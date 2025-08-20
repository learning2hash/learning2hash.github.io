---
layout: publication
title: Measuring Similarity Between Embedding Spaces Using Induced Neighborhood Graphs
authors: Tiago F. Tavares, Fabio Ayres, Paris Smaragdis
conference: Arxiv
year: 2024
bibkey: tavares2024measuring
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.08687'}]
tags: [Datasets, Evaluation, Distance Metric Learning, Few-shot & Zero-shot, Neural
    Hashing]
short_authors: Tiago F. Tavares, Fabio Ayres, Paris Smaragdis
---
Deep Learning techniques have excelled at generating embedding spaces that
capture semantic similarities between items. Often these representations are
paired, enabling experiments with analogies (pairs within the same domain) and
cross-modality (pairs across domains). These experiments are based on specific
assumptions about the geometry of embedding spaces, which allow finding paired
items by extrapolating the positional relationships between embedding pairs in
the training dataset, allowing for tasks such as finding new analogies, and
multimodal zero-shot classification. In this work, we propose a metric to
evaluate the similarity between paired item representations. Our proposal is
built from the structural similarity between the nearest-neighbors induced
graphs of each representation, and can be configured to compare spaces based on
different distance metrics and on different neighborhood sizes. We demonstrate
that our proposal can be used to identify similar structures at different
scales, which is hard to achieve with kernel methods such as Centered Kernel
Alignment (CKA). We further illustrate our method with two case studies: an
analogy task using GloVe embeddings, and zero-shot classification in the
CIFAR-100 dataset using CLIP embeddings. Our results show that accuracy in both
analogy and zero-shot classification tasks correlates with the embedding
similarity. These findings can help explain performance differences in these
tasks, and may lead to improved design of paired-embedding models in the
future.