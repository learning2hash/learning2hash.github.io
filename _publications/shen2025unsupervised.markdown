---
layout: publication
title: Unsupervised Deep Hashing With Similarity-adaptive And Discrete Optimization
authors: Fumin Shen, Xu, Liu, Yang, Huang, Shen
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2025
bibkey: shen2025unsupervised
citations: 395
additional_links: [{name: Paper, url: 'http://cfm.uestc.edu.cn/~fshen/SADH.pdf'}]
tags: ["Compact Codes", "Hashing Methods", "Neural Hashing", "Unsupervised"]
short_authors: Shen et al.
---
Recent vision and learning studies show that learning compact hash codes can facilitate massive data processing
with significantly reduced storage and computation. Particularly, learning deep hash functions has greatly improved the retrieval
performance, typically under the semantic supervision. In contrast, current unsupervised deep hashing algorithms can hardly achieve
satisfactory performance due to either the relaxed optimization or absence of similarity-sensitive objective. In this work, we propose a
simple yet effective unsupervised hashing framework, named Similarity-Adaptive Deep Hashing (SADH), which alternatingly proceeds
over three training modules: deep hash model training, similarity graph updating and binary code optimization. The key difference from
the widely-used two-step hashing method is that the output representations of the learned deep model help update the similarity graph
matrix, which is then used to improve the subsequent code optimization. In addition, for producing high-quality binary codes, we devise
an effective discrete optimization algorithm which can directly handle the binary constraints with a general hashing loss. Extensive
experiments validate the efficacy of SADH, which consistently outperforms the state-of-the-arts by large gaps.