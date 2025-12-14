---
layout: publication
title: 'MERIT: Multilingual Semantic Retrieval With Interleaved Multi-condition Query'
authors: Wei Chow, Yuan Gao, Linfeng Li, Xian Wang, Qi Xu, Hang Song, Lingdong Kong,
  Ran Zhou, Yi Zeng, Yidong Cai, Botian Jiang, Shilin Xu, Jiajun Zhang, Minghui Qiu,
  Xiangtai Li, Tianshu Yang, Siliang Tang, Juncheng Li
conference: Arxiv
year: 2025
bibkey: chow2025merit
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.03144'}]
tags: [Evaluation, Tools & Libraries, Datasets, Self-Supervised]
short_authors: Chow et al.
---
Semantic retrieval is crucial for modern applications yet remains underexplored in current research. Existing datasets are limited to single languages, single images, or singular retrieval conditions, often failing to fully exploit the expressive capacity of visual information as evidenced by maintained performance when images are replaced with captions. However, practical retrieval scenarios frequently involve interleaved multi-condition queries with multiple images. Hence, this paper introduces MERIT, the first multilingual dataset for interleaved multi-condition semantic retrieval, comprising 320,000 queries with 135,000 products in 5 languages, covering 7 distinct product categories. Extensive experiments on MERIT identify existing models's limitation: focusing solely on global semantic information while neglecting specific conditional elements in queries. Consequently, we propose Coral, a novel fine-tuning framework that adapts pre-trained MLLMs by integrating embedding reconstruction to preserve fine-grained conditional elements and contrastive learning to extract comprehensive global semantics. Experiments demonstrate that Coral achieves a 45.9% performance improvement over conventional approaches on MERIT, with strong generalization capabilities validated across 8 established retrieval benchmarks. Collectively, our contributions - a novel dataset, identification of critical limitations in existing approaches, and an innovative fine-tuning framework - establish a foundation for future research in interleaved multi-condition semantic retrieval.