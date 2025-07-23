---
layout: publication
title: Cross-domain Diffusion With Progressive Alignment For Efficient Adaptive Retrieval
authors: Luo Junyu, Zhao Yusheng, Luo Xiao, Xiao Zhiping, Ju Wei, Shen Li, Tao Dacheng,
  Zhang Ming
conference: IEEE Transactions on Image Processing
year: 2025
bibkey: luo2025cross
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.13907'}]
tags: ["Efficiency", "Evaluation", "Hashing Methods", "Image Retrieval", "Memory Efficiency", "Multimodal Retrieval", "Scalability"]
short_authors: Luo et al.
---
Unsupervised efficient domain adaptive retrieval aims to transfer knowledge from a labeled source domain to an unlabeled target domain, while maintaining low storage cost and high retrieval efficiency. However, existing methods typically fail to address potential noise in the target domain, and directly align high-level features across domains, thus resulting in suboptimal retrieval performance. To address these challenges, we propose a novel Cross-Domain Diffusion with Progressive Alignment method (COUPLE). This approach revisits unsupervised efficient domain adaptive retrieval from a graph diffusion perspective, simulating cross-domain adaptation dynamics to achieve a stable target domain adaptation process. First, we construct a cross-domain relationship graph and leverage noise-robust graph flow diffusion to simulate the transfer dynamics from the source domain to the target domain, identifying lower noise clusters. We then leverage the graph diffusion results for discriminative hash code learning, effectively learning from the target domain while reducing the negative impact of noise. Furthermore, we employ a hierarchical Mixup operation for progressive domain alignment, which is performed along the cross-domain random walk paths. Utilizing target domain discriminative hash learning and progressive domain alignment, COUPLE enables effective domain adaptive hash learning. Extensive experiments demonstrate COUPLE's effectiveness on competitive benchmarks.