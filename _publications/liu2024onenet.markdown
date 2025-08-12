---
layout: publication
title: 'Onenet: A Fine-tuning Free Framework For Few-shot Entity Linking Via Large
  Language Model Prompting'
authors: Xukai Liu, Ye Liu, Kai Zhang, Kehang Wang, Qi Liu, Enhong Chen
conference: Proceedings of the 2024 Conference on Empirical Methods in Natural Language
  Processing
year: 2024
bibkey: liu2024onenet
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.07549'}]
tags: ["EMNLP", "Few Shot & Zero Shot"]
short_authors: Liu et al.
---
Entity Linking (EL) is the process of associating ambiguous textual mentions
to specific entities in a knowledge base. Traditional EL methods heavily rely
on large datasets to enhance their performance, a dependency that becomes
problematic in the context of few-shot entity linking, where only a limited
number of examples are available for training. To address this challenge, we
present OneNet, an innovative framework that utilizes the few-shot learning
capabilities of Large Language Models (LLMs) without the need for fine-tuning.
To the best of our knowledge, this marks a pioneering approach to applying LLMs
to few-shot entity linking tasks. OneNet is structured around three key
components prompted by LLMs: (1) an entity reduction processor that simplifies
inputs by summarizing and filtering out irrelevant entities, (2) a
dual-perspective entity linker that combines contextual cues and prior
knowledge for precise entity linking, and (3) an entity consensus judger that
employs a unique consistency algorithm to alleviate the hallucination in the
entity linking reasoning. Comprehensive evaluations across seven benchmark
datasets reveal that OneNet outperforms current state-of-the-art entity linking
methods.