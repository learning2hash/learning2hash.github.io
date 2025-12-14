---
layout: publication
title: 'HATA: Trainable And Hardware-efficient Hash-aware Top-k Attention For Scalable
  Large Model Inference'
authors: Ping Gong, Jiawei Yi, Shengnan Wang, Juncheng Zhang, Zewen Jin, Ouxiang Zhou,
  Ruibo Liu, Guanbin Xu, Youhui Bai, Bowen Ye, Kun Yuan, Tong Yang, Gong Zhang, Renhai
  Chen, Feng Wu, Cheng Li
conference: 'Findings of the Association for Computational Linguistics: ACL 2025'
year: 2025
bibkey: gong2025hata
citations: 0
additional_links: [{name: Code, url: 'https://github.com/gpzlx1/HATA'}, {name: Paper,
    url: 'https://arxiv.org/abs/2506.02572'}]
tags: [Hashing Methods, Efficiency, ACL]
short_authors: Gong et al.
---
Large Language Models (LLMs) have emerged as a pivotal research area, yet the attention module remains a critical bottleneck in LLM inference, even with techniques like KVCache to mitigate redundant computations. While various top-\(k\) attention mechanisms have been proposed to accelerate LLM inference by exploiting the inherent sparsity of attention, they often struggled to strike a balance between efficiency and accuracy. In this paper, we introduce HATA (Hash-Aware Top-\(k\) Attention), a novel approach that systematically integrates low-overhead learning-to-hash techniques into the Top-\(k\) attention process. Different from the existing top-k attention methods which are devoted to seeking an absolute estimation of qk score, typically with a great cost, HATA maps queries and keys into binary hash codes, and acquires the relative qk score order with a quite low cost, which is sufficient for realizing top-k attention. Extensive experiments demonstrate that HATA achieves up to 7.2\(\times\) speedup compared to vanilla full attention while maintaining model accuracy. In addition, HATA outperforms the state-of-the-art top-\(k\) attention methods in both accuracy and efficiency across multiple mainstream LLM models and diverse tasks. HATA is open source at https://github.com/gpzlx1/HATA.