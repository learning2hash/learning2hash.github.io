---
layout: publication
title: Deep Class-guided Hashing For Multi-label Cross-modal Retrieval
authors: Hao Chen, Lei Zhu, Xinghui Zhu
conference: Applied Sciences
year: 2025
bibkey: chen2024deep
citations: 2
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/2410.15387'}]
tags: ["Datasets", "Evaluation", "Hashing Methods", "Multimodal Retrieval", "Neural Hashing", "Similarity Search", "Tools & Libraries"]
short_authors: Hao Chen, Lei Zhu, Xinghui Zhu
---
Deep hashing, due to its low cost and efficient retrieval advantages, is
widely valued in cross-modal retrieval. However, existing cross-modal hashing
methods either explore the relationships between data points, which inevitably
leads to intra-class dispersion, or explore the relationships between data
points and categories while ignoring the preservation of inter-class structural
relationships, resulting in the generation of suboptimal hash codes. How to
maintain both intra-class aggregation and inter-class structural relationships,
In response to this issue, this paper proposes a DCGH method. Specifically, we
use proxy loss as the mainstay to maintain intra-class aggregation of data,
combined with pairwise loss to maintain inter-class structural relationships,
and on this basis, further propose a variance constraint to address the
semantic bias issue caused by the combination. A large number of comparative
experiments on three benchmark datasets show that the DCGH method has
comparable or even better performance compared to existing cross-modal
retrieval methods. The code for the implementation of our DCGH framework is
available at https://github.com/donnotnormal/DCGH.