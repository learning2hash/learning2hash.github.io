---
layout: publication
title: 'Docscan: Unsupervised Text Classification Via Learning From Neighbors'
authors: Dominik Stammbach, Elliott Ash
conference: in Proceedings of the 18th Conference on Natural Language Processing (KONVENS
  2022) pages 21-28 Potsdam Germany
year: 2021
bibkey: stammbach2021docscan
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.04024'}]
tags: ["Datasets", "Evaluation", "Supervised", "Unsupervised"]
short_authors: Dominik Stammbach, Elliott Ash
---
We introduce DocSCAN, a completely unsupervised text classification approach
using Semantic Clustering by Adopting Nearest-Neighbors (SCAN). For each
document, we obtain semantically informative vectors from a large pre-trained
language model. Similar documents have proximate vectors, so neighbors in the
representation space tend to share topic labels. Our learnable clustering
approach uses pairs of neighboring datapoints as a weak learning signal. The
proposed approach learns to assign classes to the whole dataset without
provided ground-truth labels. On five topic classification benchmarks, we
improve on various unsupervised baselines by a large margin. In datasets with
relatively few and balanced outcome classes, DocSCAN approaches the performance
of supervised classification. The method fails for other types of
classification, such as sentiment analysis, pointing to important conceptual
and practical differences between classifying images and texts.