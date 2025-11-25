---
layout: publication
title: 'A Recipe For Efficient SBIR Models: Combining Relative Triplet Loss With Batch
  Normalization And Knowledge Distillation'
authors: "Omar Seddati, Nathan Hubens, St\xE9phane Dupont, Thierry Dutoit"
conference: Arxiv
year: 2023
bibkey: seddati2023a
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.18988'}]
tags: ["Distance Metric Learning", "Evaluation", "Image Retrieval"]
short_authors: Seddati et al.
---
Sketch-Based Image Retrieval (SBIR) is a crucial task in multimedia
retrieval, where the goal is to retrieve a set of images that match a given
sketch query. Researchers have already proposed several well-performing
solutions for this task, but most focus on enhancing embedding through
different approaches such as triplet loss, quadruplet loss, adding data
augmentation, and using edge extraction. In this work, we tackle the problem
from various angles. We start by examining the training data quality and show
some of its limitations. Then, we introduce a Relative Triplet Loss (RTL), an
adapted triplet loss to overcome those limitations through loss weighting based
on anchors similarity. Through a series of experiments, we demonstrate that
replacing a triplet loss with RTL outperforms previous state-of-the-art without
the need for any data augmentation. In addition, we demonstrate why batch
normalization is more suited for SBIR embeddings than l2-normalization and show
that it improves significantly the performance of our models. We further
investigate the capacity of models required for the photo and sketch domains
and demonstrate that the photo encoder requires a higher capacity than the
sketch encoder, which validates the hypothesis formulated in [34]. Then, we
propose a straightforward approach to train small models, such as ShuffleNetv2
[22] efficiently with a marginal loss of accuracy through knowledge
distillation. The same approach used with larger models enabled us to
outperform previous state-of-the-art results and achieve a recall of 62.38% at
k = 1 on The Sketchy Database [30].