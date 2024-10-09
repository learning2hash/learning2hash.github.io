---
layout: publication
title: Prefix-tuning Optimizing Continuous Prompts For Generation
authors: Xiang Lisa Li, Percy Liang
conference: "Arxiv"
year: 2021
bibkey: lisa2021prefix
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2101.00190v1"}
tags: ['ARXIV']
---
Fine-tuning is the de facto way to leverage large pretrained language models to perform downstream tasks. However it modifies all the language model parameters and therefore necessitates storing a full copy for each task. In this paper we propose prefix-tuning a lightweight alternative to fine-tuning for natural language generation tasks which keeps language model parameters frozen but optimizes a small continuous task-specific vector (called the prefix). Prefix-tuning draws inspiration from prompting allowing subsequent tokens to attend to this prefix as if it were virtual tokens. We apply prefix-tuning to GPT-2 for table-to-text generation and to BART for summarization. We find that by learning only 0.137; of the parameters prefix-tuning obtains comparable performance in the full data setting outperforms fine-tuning in low-data settings and extrapolates better to examples with topics unseen during training.
