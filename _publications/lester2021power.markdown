---
layout: publication
title: The Power Of Scale For Parameter-efficient Prompt Tuning
authors: Brian Lester, Rami Al-rfou, Noah Constant
conference: "Arxiv"
year: 2021
bibkey: lester2021power
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2104.08691v2"}
tags: ['ARXIV']
---
In this work we explore prompt tuning a simple yet effective mechanism for learning soft prompts to condition frozen language models to perform specific downstream tasks. Unlike the discrete text prompts used by GPT-3 soft prompts are learned through backpropagation and can be tuned to incorporate signal from any number of labeled examples. Our end-to-end learned approach outperforms GPT-3s few-shot learning by a large margin. More remarkably through ablations on model size using T5 we show that prompt tuning becomes more competitive with scale as models exceed billions of parameters our method closes the gap and matches the strong performance of model tuning (where all model weights are tuned). This finding is especially relevant in that large models are costly to share and serve and the ability to reuse one frozen model for multiple downstream tasks can ease this burden. Our method can be seen as a simplification of the recently proposed prefix tuning of Li and Liang (2021) and we provide a comparison to this and other similar approaches. Finally we show that conditioning a frozen model with soft prompts confers benefits in robustness to domain transfer as compared to full model tuning.
