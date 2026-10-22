# Обучение нейросетей — где учиться (Perplexity, глубокое исследование 23.10.2026)

Полная карта со ссылками — `C:\Users\User\komputer\neyroseti_obuchenie.html`. Её выбор 23.10: «настоящее обучение нейросетей» (не промпты).
- Путь: Python → Karpathy micrograd → makemore → PyTorch Learn the Basics / fast.ai → «Let's build GPT», nanoGPT (устарел, для чтения) → Hugging Face LLM Course + один LoRA в Colab/Kaggle → потом nanochat, CS336.
- Правила: Karpathy «A Recipe for Training Neural Networks»; Google «Deep Learning Tuning Playbook». Смотреть данные глазами, начать с рабочего образца, «перезубрить» одну пачку, три части данных, менять одно за раз, сохранять точки возврата, журнал опытов.
- Дообучать — только после сильного промпта и при узкой повторяющейся задаче; знания из документов — RAG, живые данные — инструменты.
- Claude: RLHF + Constitutional AI; общего способа дообучить современные модели Claude нет (Haiku 3 на Bedrock снят 10.09.2026 — по данным Perplexity). Учиться на открытых моделях.
- На ноутбуке без видеокарты: micrograd, makemore, крошечный nanoGPT на CPU; LoRA — в облачном блокноте, заранее предел трат.
