---
layout: publication
title: Hierarchical Nearest Neighbor Graph Embedding For Efficient Dimensionality
  Reduction
authors: M. Saquib Sarfraz, Marios Koulakis, Constantin Seibold, Rainer Stiefelhagen
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: sarfraz2022hierarchical
citations: 8
additional_links: [{name: Code, url: 'https://github.com/koulakis/h-nne'}, {name: Paper,
    url: 'https://arxiv.org/abs/2203.12997'}]
tags: ["CVPR", "Efficiency"]
short_authors: Sarfraz et al.
---
Dimensionality reduction is crucial both for visualization and preprocessing
high dimensional data for machine learning. We introduce a novel method based
on a hierarchy built on 1-nearest neighbor graphs in the original space which
is used to preserve the grouping properties of the data distribution on
multiple levels. The core of the proposal is an optimization-free projection
that is competitive with the latest versions of t-SNE and UMAP in performance
and visualization quality while being an order of magnitude faster in run-time.
Furthermore, its interpretable mechanics, the ability to project new data, and
the natural separation of data clusters in visualizations make it a general
purpose unsupervised dimension reduction technique. In the paper, we argue
about the soundness of the proposed method and evaluate it on a diverse
collection of datasets with sizes varying from 1K to 11M samples and dimensions
from 28 to 16K. We perform comparisons with other state-of-the-art methods on
multiple metrics and target dimensions highlighting its efficiency and
performance. Code is available at https://github.com/koulakis/h-nne