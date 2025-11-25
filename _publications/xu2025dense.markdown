---
layout: publication
title: 'Dense Retrievers Can Fail On Simple Queries: Revealing The Granularity Dilemma
  Of Embeddings'
authors: Liyan Xu, Zhenlin Su, Mo Yu, Jiangnan Li, Fandong Meng, Jie Zhou
conference: 'Findings of the Association for Computational Linguistics: EMNLP 2025'
year: 2025
bibkey: xu2025dense
citations: 0
additional_links: [{name: Code, url: 'https://github.com/lxucs/CapRetrieval'}, {name: Paper,
    url: 'https://arxiv.org/abs/2506.08592'}]
tags: ["Datasets", "EMNLP", "Evaluation"]
short_authors: Xu et al.
---
This work focuses on an observed limitation of text encoders: embeddings may not be able to recognize fine-grained entities or events within the semantics, resulting in failed dense retrieval on even simple cases. To examine such behaviors, we first introduce a new evaluation dataset in Chinese, named CapRetrieval, whose passages are image captions, and queries are phrases inquiring entities or events in various forms. Zero-shot evaluation suggests that encoders may fail on these fine-grained matching, regardless of training sources or model sizes. Aiming for enhancement, we proceed to finetune encoders with our proposed data generation strategies, which obtains the best performance on CapRetrieval. Within this process, we further identify an issue of granularity dilemma, a challenge for embeddings to express fine-grained salience while aligning with overall semantics. Our dataset, code and models in this work are publicly released at https://github.com/lxucs/CapRetrieval.