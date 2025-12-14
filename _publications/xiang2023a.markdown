---
layout: publication
title: A Long-tail Friendly Representation Framework For Artist And Music Similarity
authors: Haoran Xiang, Junyu Dai, Xuchen Song, Furao Shen
conference: Arxiv
year: 2023
bibkey: xiang2023a
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.04182'}]
tags: [Evaluation, Distance Metric Learning, Datasets, Tools & Libraries, Recommender
    Systems]
short_authors: Xiang et al.
---
The investigation of the similarity between artists and music is crucial in
music retrieval and recommendation, and addressing the challenge of the
long-tail phenomenon is increasingly important. This paper proposes a Long-Tail
Friendly Representation Framework (LTFRF) that utilizes neural networks to
model the similarity relationship. Our approach integrates music, user,
metadata, and relationship data into a unified metric learning framework, and
employs a meta-consistency relationship as a regular term to introduce the
Multi-Relationship Loss. Compared to the Graph Neural Network (GNN), our
proposed framework improves the representation performance in long-tail
scenarios, which are characterized by sparse relationships between artists and
music. We conduct experiments and analysis on the AllMusic dataset, and the
results demonstrate that our framework provides a favorable generalization of
artist and music representation. Specifically, on similar artist/music
recommendation tasks, the LTFRF outperforms the baseline by 9.69%/19.42% in Hit
Ratio@10, and in long-tail cases, the framework achieves 11.05%/14.14% higher
than the baseline in Consistent@10.