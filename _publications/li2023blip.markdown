---
layout: publication
title: BLIP-2 Bootstrapping Language-image Pre-training With Frozen Image Encoders And Large Language Models
authors: Junnan Li, Dongxu Li, Silvio Savarese, Steven Hoi
conference: "Arxiv"
year: 2023
bibkey: li2023blip
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2301.12597v3"}
tags: ['ARXIV', 'Cross Modal']
---
The cost of vision-and-language pre-training has become increasingly prohibitive due to end-to-end training of large-scale models. This paper proposes BLIP-2 a generic and efficient pre-training strategy that bootstraps vision-language pre-training from off-the-shelf frozen pre-trained image encoders and frozen large language models. BLIP-2 bridges the modality gap with a lightweight Querying Transformer which is pre-trained in two stages. The first stage bootstraps vision-language representation learning from a frozen image encoder. The second stage bootstraps vision-to-language generative learning from a frozen language model. BLIP-2 achieves state-of-the-art performance on various vision-language tasks despite having significantly fewer trainable parameters than existing methods. For example our model outperforms Flamingo80B by 8.737; on zero-shot VQAv2 with 54x fewer trainable parameters. We also demonstrate the models emerging capabilities of zero-shot image-to-text generation that can follow natural language instructions.
