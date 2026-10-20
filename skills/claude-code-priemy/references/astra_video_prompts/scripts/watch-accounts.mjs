#!/usr/bin/env node
/**
 * Watch X accounts for new video-prompt posts.
 *
 * Reads  watch/accounts.json   — who to watch, what keywords count
 * Writes watch/seen.json       — post ids already handled
 * Emits  GitHub Issues         — one per new matching post
 *        Discord / Telegram    — optional, via repo secrets
 *
 * First run writes a baseline and opens nothing. That is intentional:
 * without it, the first run would file an Issue for every post in history.
 *
 * Env:
 *   GITHUB_TOKEN        required to open Issues
 *   GITHUB_REPOSITORY   owner/repo, provided by Actions
 *   RSSHUB_BASE         default https://rsshub.app
 *   DISCORD_WEBHOOK_URL optional
 *   TELEGRAM_BOT_TOKEN  optional (with TELEGRAM_CHAT_ID)
 *   TELEGRAM_CHAT_ID    optional
 *   DRY_RUN=1           print, don't post
 */

import fs from "node:fs/promises";
import path from "node:path";

const ROOT = path.resolve(import.meta.dirname, "..");
const ACCOUNTS_FILE = path.join(ROOT, "watch", "accounts.json");
const SEEN_FILE = path.join(ROOT, "watch", "seen.json");

const RSSHUB_BASE = (process.env.RSSHUB_BASE || "https://rsshub.app").replace(/\/$/, "");
const GITHUB_TOKEN = process.env.GITHUB_TOKEN;
const GITHUB_REPOSITORY = process.env.GITHUB_REPOSITORY;
const DISCORD_WEBHOOK_URL = process.env.DISCORD_WEBHOOK_URL;
const TELEGRAM_BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN;
const TELEGRAM_CHAT_ID = process.env.TELEGRAM_CHAT_ID;
const DRY_RUN = process.env.DRY_RUN === "1";

const MAX_ISSUES_PER_RUN = 10; // don't flood the tracker if a watch breaks

const log = (...a) => console.log("[watch]", ...a);

const readJson = async (p, fallback) => {
  try {
    return JSON.parse(await fs.readFile(p, "utf8"));
  } catch (e) {
    if (e.code === "ENOENT") return fallback;
    throw e;
  }
};

const stripHtml = (s = "") =>
  s
    .replace(/<br\s*\/?>/gi, "\n")
    .replace(/<[^>]+>/g, "")
    .replace(/&nbsp;/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/\n{3,}/g, "\n\n")
    .trim();

async function fetchAccount(handle, pathTemplate) {
  const url = RSSHUB_BASE + pathTemplate.replace("{handle}", encodeURIComponent(handle));
  const res = await fetch(url, {
    headers: { "User-Agent": "awesome-astra-video-prompts-watcher/1.0" },
    signal: AbortSignal.timeout(30_000),
  });
  if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);

  const body = await res.text();
  let items = [];
  try {
    const data = JSON.parse(body);
    items = data.items || [];
  } catch {
    // RSSHub returned XML despite format=json — parse the feed loosely.
    items = [...body.matchAll(/<item>([\s\S]*?)<\/item>/g)].map((m) => {
      const block = m[1];
      const pick = (tag) => {
        const re = new RegExp(`<${tag}[^>]*>([\\s\\S]*?)</${tag}>`);
        const hit = block.match(re);
        if (!hit) return "";
        return hit[1].replace(/^<!\[CDATA\[/, "").replace(/\]\]>$/, "").trim();
      };
      return {
        id: pick("guid") || pick("link"),
        url: pick("link"),
        title: pick("title"),
        content_html: pick("description"),
        date_published: pick("pubDate"),
      };
    });
  }

  return items.map((it) => ({
    id: String(it.id || it.url || it.title || "").trim(),
    url: it.url || it.id || "",
    text: stripHtml(it.content_html || it.content_text || it.title || ""),
    date: it.date_published || it.date_modified || "",
  }));
}

const matchesKeywords = (text, keywords) => {
  if (!keywords || keywords.length === 0) return true; // empty filter = keep everything
  const hay = text.toLowerCase();
  return keywords.filter((k) => hay.includes(String(k).toLowerCase()));
};

async function openIssue({ account, item, hits }) {
  const title = `[watch] ${account.name || account.handle}: ${item.text.slice(0, 60).replace(/\s+/g, " ")}…`;
  const body = [
    `**Account:** [@${account.handle}](https://x.com/${account.handle})`,
    account.why ? `**Why we watch:** ${account.why}` : null,
    `**Posted:** ${item.date || "unknown"}`,
    hits.length ? `**Matched:** ${hits.join(", ")}` : null,
    "",
    "---",
    "",
    "```",
    item.text.slice(0, 4000),
    "```",
    "",
    `[Original post](${item.url})`,
    "",
    "---",
    "",
    "**To close this out:**",
    "",
    "- [ ] Is this actually a prompt worth keeping? (Closing as *not a prompt* is fine.)",
    "- [ ] File it under the right `prompts/` folder with a full YAML header",
    "- [ ] Set `completeness` honestly — don't reconstruct missing parts",
    "- [ ] Update `sources/completeness.md`",
  ]
    .filter(Boolean)
    .join("\n");

  if (DRY_RUN || !GITHUB_TOKEN || !GITHUB_REPOSITORY) {
    log("DRY RUN issue:", title);
    return;
  }

  const res = await fetch(`https://api.github.com/repos/${GITHUB_REPOSITORY}/issues`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${GITHUB_TOKEN}`,
      Accept: "application/vnd.github+json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title, body, labels: ["watch", "prompt-candidate"] }),
  });
  if (!res.ok) log("issue failed:", res.status, (await res.text()).slice(0, 200));
  else log("issue opened:", title);
}

async function notify(text) {
  if (DRY_RUN) return;
  if (DISCORD_WEBHOOK_URL) {
    await fetch(DISCORD_WEBHOOK_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ content: text.slice(0, 1900) }),
    }).catch((e) => log("discord failed:", e.message));
  }
  if (TELEGRAM_BOT_TOKEN && TELEGRAM_CHAT_ID) {
    await fetch(`https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        chat_id: TELEGRAM_CHAT_ID,
        text: text.slice(0, 4000),
        disable_web_page_preview: false,
      }),
    }).catch((e) => log("telegram failed:", e.message));
  }
}

async function main() {
  const config = await readJson(ACCOUNTS_FILE, null);
  if (!config) throw new Error(`missing ${ACCOUNTS_FILE}`);

  const seen = await readJson(SEEN_FILE, { bootstrapped: false, ids: {} });
  const bootstrapping = !seen.bootstrapped;
  if (bootstrapping) log("first run — writing baseline, opening nothing");

  const template = config.rsshubPathTemplate || "/twitter/user/{handle}?format=json&limit=20";
  const keywords = config.keywordFilter || [];
  let opened = 0;

  for (const account of config.accounts || []) {
    let items;
    try {
      items = await fetchAccount(account.handle, template);
      log(`@${account.handle}: ${items.length} items`);
    } catch (e) {
      log(`@${account.handle}: fetch failed — ${e.message}`);
      continue;
    }

    for (const item of items) {
      if (!item.id || seen.ids[item.id]) continue;

      const hits = matchesKeywords(item.text, keywords);
      seen.ids[item.id] = new Date().toISOString().slice(0, 10);

      if (bootstrapping) continue;
      if (!hits || hits.length === 0) continue;
      if (opened >= MAX_ISSUES_PER_RUN) {
        log("hit per-run issue cap, remaining posts marked seen");
        continue;
      }

      await openIssue({ account, item, hits });
      await notify(`New prompt candidate from @${account.handle}\n${item.url}`);
      opened++;
    }

    await new Promise((r) => setTimeout(r, 1500)); // be polite to RSSHub
  }

  seen.bootstrapped = true;
  if (!DRY_RUN) await fs.writeFile(SEEN_FILE, JSON.stringify(seen, null, 2) + "\n");
  log(`done — ${opened} issue(s), ${Object.keys(seen.ids).length} ids tracked`);
}

main().catch((e) => {
  console.error("[watch] fatal:", e);
  process.exit(1);
});
