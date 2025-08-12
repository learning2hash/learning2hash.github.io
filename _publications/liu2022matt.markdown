---
layout: publication
title: 'MATT: A Multiple-instance Attention Mechanism For Long-tail Music Genre Classification'
authors: Xiaokai Liu, Menghua Zhang
conference: Arxiv
year: 2022
bibkey: liu2022matt
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.04109'}]
tags: []
short_authors: Xiaokai Liu, Menghua Zhang
---
Imbalanced music genre classification is a crucial task in the Music
Information Retrieval (MIR) field for identifying the long-tail, data-poor
genre based on the related music audio segments, which is very prevalent in
real-world scenarios. Most of the existing models are designed for
class-balanced music datasets, resulting in poor performance in accuracy and
generalization when identifying the music genres at the tail of the
distribution. Inspired by the success of introducing Multi-instance Learning
(MIL) in various classification tasks, we propose a novel mechanism named
Multi-instance Attention (MATT) to boost the performance for identifying tail
classes. Specifically, we first construct the bag-level datasets by generating
the album-artist pair bags. Second, we leverage neural networks to encode the
music audio segments. Finally, under the guidance of a multi-instance attention
mechanism, the neural network-based models could select the most informative
genre to match the given music segment. Comprehensive experimental results on a
large-scale music genre benchmark dataset with long-tail distribution
demonstrate MATT significantly outperforms other state-of-the-art baselines.