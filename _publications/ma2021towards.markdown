---
layout: publication
title: 'Towards Clustering-friendly Representations: Subspace Clustering Via Graph
  Filtering'
authors: Zhengrui Ma, Zhao Kang, Guangchun Luo, Ling Tian
conference: Arxiv
year: 2021
bibkey: ma2021towards
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.09874'}]
tags: []
short_authors: Ma et al.
---
Finding a suitable data representation for a specific task has been shown to
be crucial in many applications. The success of subspace clustering depends on
the assumption that the data can be separated into different subspaces.
However, this simple assumption does not always hold since the raw data might
not be separable into subspaces. To recover the ``clustering-friendly''
representation and facilitate the subsequent clustering, we propose a graph
filtering approach by which a smooth representation is achieved. Specifically,
it injects graph similarity into data features by applying a low-pass filter to
extract useful data representations for clustering. Extensive experiments on
image and document clustering datasets demonstrate that our method improves
upon state-of-the-art subspace clustering techniques. Especially, its
comparable performance with deep learning methods emphasizes the effectiveness
of the simple graph filtering scheme for many real-world applications. An
ablation study shows that graph filtering can remove noise, preserve structure
in the image, and increase the separability of classes.