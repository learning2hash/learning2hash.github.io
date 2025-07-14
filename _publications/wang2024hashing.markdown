---
layout: publication
title: Hashing with Uncertainty Quantification via Sampling-based Hypothesis Testing
authors: Yucheng Wang, Mingyuan Zhou, Xiaoning Qian
conference: TMLR
year: 2024
citations: 0
bibkey: wang2024hashing
additional_links: [{name: Paper, url: 'https://dl.acm.org/citation.cfm?id=3240547'},
  {name: Code, url: 'https://github.com/QianLab/HashUQ'}]
tags: [TMLR, Supervised, Has Code]
---
To quantify different types of uncertainty when deriving hash-codes for image retrieval, we develop a probabilistic hashing model(ProbHash). 
Sampling-based hypothesis testing is then derived for hashing with uncertainty quantification(HashUQ) in ProbHash to improve the granularity of hashing-based retrieval by prioritizing the data with confident hash-codes. HashUQ can drastically improve the retrieval performance without sacrificing computational efficiency. For efficient deployment of HashUQ in real-world applications, we discretize the quantified uncertainty to reduce the potential storage overhead. Experimental results show that our HashUQ can achieve state-of-the-art retrieval performance on three image datasets. Ablation experiments on model hyperparameters, different model components, and effects of UQ are also provided with performance comparisons. Our code is available at https://github.com/QianLab/HashUQ.