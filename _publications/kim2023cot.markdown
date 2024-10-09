---
layout: publication
title: The Cot Collection Improving Zero-shot And Few-shot Learning Of Language Models Via Chain-of-thought Fine-tuning
authors: Seungone Kim, Se June Joo, Doyoung Kim, Joel Jang, Seonghyeon Ye, Jamin Shin, Minjoon Seo
conference: "Arxiv"
year: 2023
bibkey: kim2023cot
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2305.14045v2"}
tags: ['ARXIV']
---
Language models (LMs) with less than 100B parameters are known to perform poorly on chain-of-thought (CoT) reasoning in contrast to large LMs when solving unseen tasks. In this work we aim to equip smaller LMs with the step-by-step reasoning capability by instruction tuning with CoT rationales. In order to achieve this goal we first introduce a new instruction-tuning dataset called the CoT Collection which augments the existing Flan Collection (including only 9 CoT tasks) with additional 1.84 million rationales across 1060 tasks. We show that CoT fine-tuning Flan-T5 (3B amp; 11B) with CoT Collection enables smaller LMs to have better CoT capabilities on unseen tasks. On the BIG-Bench-Hard (BBH) benchmark we report an average improvement of +4.3437; (Flan-T5 3B) and +2.6037; (Flan-T5 11B) in terms of zero-shot task accuracy. Furthermore we show that instruction tuning with CoT Collection allows LMs to possess stronger few-shot learning capabilities on 4 domain-specific tasks resulting in an improvement of +2.2437; (Flan-T5 3B) and +2.3737; (Flan-T5 11B) even outperforming ChatGPT utilizing demonstrations until the max length by a +13.9837; margin. Our code the CoT Collection data and model checkpoints are publicly available.
