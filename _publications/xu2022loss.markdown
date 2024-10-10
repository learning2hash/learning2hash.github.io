---
layout: publication
title: Hyp(^2) Loss Beyond Hypersphere Metric Space For Multi-label Image Retrieval
authors: Xu Chengyin, Chai Zenghao, Xu Zhengzhuo, Yuan Chun, Fan Yanbo, Wang Jue
conference: "Arxiv"
year: 2022
bibkey: xu2022loss
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2208.06866"}
  - {name: "Code", url: "https://github.com/JerryXu0129/HyP2-Loss"}
tags: ['ARXIV', 'Has Code', 'Image Retrieval']
---
Image retrieval has become an increasingly appealing technique with broad multimedia application prospects where deep hashing serves as the dominant branch towards low storage and efficient retrieval. In this paper we carried out in-depth investigations on metric learning in deep hashing for establishing a powerful metric space in multi-label scenarios where the pair loss suffers high computational overhead and converge difficulty while the proxy loss is theoretically incapable of expressing the profound label dependencies and exhibits conflicts in the constructed hypersphere space. To address the problems we propose a novel metric learning framework with Hybrid Proxy-Pair Loss (HyP(^2) Loss) that constructs an expressive metric space with efficient training complexity w.r.t. the whole dataset. The proposed HyP(^2) Loss focuses on optimizing the hypersphere space by learnable proxies and excavating data-to-data correlations of irrelevant pairs which integrates sufficient data correspondence of pair-based methods and high-efficiency of proxy-based methods. Extensive experiments on four standard multi-label benchmarks justify the proposed method outperforms the state-of-the-art is robust among different hash bits and achieves significant performance gains with a faster more stable convergence speed. Our code is available at https://github.com/JerryXu0129/HyP2-Loss.
