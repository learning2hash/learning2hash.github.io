---
layout: publication
title: Hierarchical Proxy-based Loss For Deep Metric Learning
authors: Zhibo Yang, Muhammet Bastan, Xinliang Zhu, Doug Gray, Dimitris Samaras
conference: Arxiv
year: 2021
bibkey: yang2021hierarchical
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.13538'}]
tags: ["Datasets", "Distance Metric Learning", "Image Retrieval"]
short_authors: Yang et al.
---
Proxy-based metric learning losses are superior to pair-based losses due to
their fast convergence and low training complexity. However, existing
proxy-based losses focus on learning class-discriminative features while
overlooking the commonalities shared across classes which are potentially
useful in describing and matching samples. Moreover, they ignore the implicit
hierarchy of categories in real-world datasets, where similar subordinate
classes can be grouped together. In this paper, we present a framework that
leverages this implicit hierarchy by imposing a hierarchical structure on the
proxies and can be used with any existing proxy-based loss. This allows our
model to capture both class-discriminative features and class-shared
characteristics without breaking the implicit data hierarchy. We evaluate our
method on five established image retrieval datasets such as In-Shop and SOP.
Results demonstrate that our hierarchical proxy-based loss framework improves
the performance of existing proxy-based losses, especially on large datasets
which exhibit strong hierarchical structure.