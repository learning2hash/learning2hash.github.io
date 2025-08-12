---
layout: publication
title: Simple Semantic-aided Few-shot Learning
authors: Hai Zhang, Junzhe Xu, Shanlin Jiang, Zhenan He
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: zhang2023simple
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.18649'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Zhang et al.
---
Learning from a limited amount of data, namely Few-Shot Learning, stands out
as a challenging computer vision task. Several works exploit semantics and
design complicated semantic fusion mechanisms to compensate for rare
representative features within restricted data. However, relying on naive
semantics such as class names introduces biases due to their brevity, while
acquiring extensive semantics from external knowledge takes a huge time and
effort. This limitation severely constrains the potential of semantics in
Few-Shot Learning. In this paper, we design an automatic way called Semantic
Evolution to generate high-quality semantics. The incorporation of high-quality
semantics alleviates the need for complex network structures and learning
algorithms used in previous works. Hence, we employ a simple two-layer network
termed Semantic Alignment Network to transform semantics and visual features
into robust class prototypes with rich discriminative features for few-shot
classification. The experimental results show our framework outperforms all
previous methods on six benchmarks, demonstrating a simple network with
high-quality semantics can beat intricate multi-modal modules on few-shot
classification tasks. Code is available at
https://github.com/zhangdoudou123/SemFew.