---
layout: publication
title: Symbol Tuning Improves In-context Learning In Language Models
authors: Jerry Wei, Le Hou, Andrew Lampinen, Xiangning Chen, Da Huang, Yi Tay, Xinyun Chen, Yifeng Lu, Denny Zhou, Tengyu Ma, Quoc V. Le
conference: "Arxiv"
year: 2023
bibkey: wei2023symbol
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2305.08298v2"}
tags: ['ARXIV']
---
We present symbol tuning - finetuning language models on in-context input-label pairs where natural language labels (e.g. positive/negative sentiment) are replaced with arbitrary symbols (e.g. foo/bar). Symbol tuning leverages the intuition that when a model cannot use instructions or natural language labels to figure out a task it must instead do so by learning the input-label mappings. We experiment with symbol tuning across Flan-PaLM models up to 540B parameters and observe benefits across various settings. First symbol tuning boosts performance on unseen in-context learning tasks and is much more robust to underspecified prompts such as those without instructions or without natural language labels. Second symbol-tuned models are much stronger at algorithmic reasoning tasks with up to 18.237; better performance on the List Functions benchmark and up to 15.337; better performance on the Simple Turing Concepts benchmark. Finally symbol-tuned models show large improvements in following flipped-labels presented in-context meaning that they are more capable of using in-context information to override prior semantic knowledge.
