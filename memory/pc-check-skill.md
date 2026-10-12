---
name: pc-check-skill
description: Скилл pc-check — проверка ПК на вирусы/майнеры/шпионов отчётом; что уже найдено 07.10.2026 и что удалено
metadata:
  node_type: memory
  type: project
  originSessionId: 0c3f2f3e-e207-49c7-b4d7-bc13b2e2a12c
  modified: 2026-10-07T15:09:58.482Z
---

«Проверь комп» = скилл pc-check (`~\.claude\skills\pc-check`), запуск от администратора без песочницы, отчёт в `C:\Users\User\pc_check\reports`. Скрипт только смотрит, удаление — после её «да».

07.10.2026 удалены: RuDesktop, MuseHub, остатки Яндекс.Диска, AlibabaProtect (служба, драйвер AliPaladin; папку дочистит задача CleanupLeftovers после перезагрузки). Edge не удаляется в РФ/US — только убран из автозагрузки. OneDrive не тронут, ей объяснено, что это.

Тогда же по её «удаляй» убраны: SoftEther VPN Server, задача AliUpdater + папки Ali1688Buyer, KMS-активатор Windows/Office, 962 строки блокировки Adobe в hosts (копия в pc_check\hosts_backup_*). Открыто: 4 бесплатных VPN-расширения в Chrome (в отчёте 07.10 вечером видны только ЮБуст и Browsec).

07.10.2026 вечером: полная проверка Защитником (57 мин) — угроз 0. По её «удали» убраны остатки Ali (WW1688CEF, Ali1688BuyerData, aliim, ProgramData\Alibaba, задача AliProctectUpdate) и McAfee WebAdvisor (программа, служба, записи реестра Chrome). Хвост: расширение McAfee уйдёт из 3 профилей Chrome после перезапуска Chrome — при следующей проверке убедиться, что его нет.

**Why:** чтобы не переспрашивать и не пугать повторно известными находками (Adobe в hosts, KMS-активатор).
**How to apply:** при новой проверке сравнивать с этим списком и говорить только о новом. Связано: [[razresheniya-ne-sprashivat]].
