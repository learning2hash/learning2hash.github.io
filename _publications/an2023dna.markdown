---
layout: publication
title: 'DNA: Denoised Neighborhood Aggregation For Fine-grained Category Discovery'
authors: Wenbin An, Feng Tian, Wenkai Shi, Yan Chen, Qinghua Zheng, Qianying Wang,
  Ping Chen
conference: Proceedings of the 2023 Conference on Empirical Methods in Natural Language
  Processing
year: 2023
bibkey: an2023dna
citations: 2
additional_links: [{name: Code, url: 'https://github.com/Lackel/DNA.'}, {name: Paper,
    url: 'https://arxiv.org/abs/2310.10151'}]
tags: ["Datasets", "EMNLP", "Evaluation", "Self-Supervised", "Supervised", "Tools & Libraries"]
short_authors: An et al.
---
Discovering fine-grained categories from coarsely labeled data is a practical
and challenging task, which can bridge the gap between the demand for
fine-grained analysis and the high annotation cost. Previous works mainly focus
on instance-level discrimination to learn low-level features, but ignore
semantic similarities between data, which may prevent these models learning
compact cluster representations. In this paper, we propose Denoised
Neighborhood Aggregation (DNA), a self-supervised framework that encodes
semantic structures of data into the embedding space. Specifically, we retrieve
k-nearest neighbors of a query as its positive keys to capture semantic
similarities between data and then aggregate information from the neighbors to
learn compact cluster representations, which can make fine-grained categories
more separatable. However, the retrieved neighbors can be noisy and contain
many false-positive keys, which can degrade the quality of learned embeddings.
To cope with this challenge, we propose three principles to filter out these
false neighbors for better representation learning. Furthermore, we
theoretically justify that the learning objective of our framework is
equivalent to a clustering loss, which can capture semantic similarities
between data to form compact fine-grained clusters. Extensive experiments on
three benchmark datasets show that our method can retrieve more accurate
neighbors (21.31% accuracy improvement) and outperform state-of-the-art models
by a large margin (average 9.96% improvement on three metrics). Our code and
data are available at https://github.com/Lackel/DNA.