---
layout: publication
title: 'Aggregating Deep Convolutional Features For Image Retrieval'
authors: Artem Babenko, Victor Lempitsky
conference: "Arxiv"
year: 2015
citations: 235
bibkey: babenko2015aggregating
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1510.07493'}
tags: ['Cross-Modal', 'Retrieval Models', 'Evaluation', 'Shallow', 'Supervised', 'Applications']
---
Several recent works have shown that image descriptors produced by deep
convolutional neural networks provide state-of-the-art performance for image
classification and retrieval problems. It has also been shown that the
activations from the convolutional layers can be interpreted as local features
describing particular image regions. These local features can be aggregated
using aggregation approaches developed for local features (e.g. Fisher
vectors), thus providing new powerful global descriptors.
  In this paper we investigate possible ways to aggregate local deep features
to produce compact global descriptors for image retrieval. First, we show that
deep features and traditional hand-engineered features have quite different
distributions of pairwise similarities, hence existing aggregation methods have
to be carefully re-evaluated. Such re-evaluation reveals that in contrast to
shallow features, the simple aggregation method based on sum pooling provides
arguably the best performance for deep convolutional features. This method is
efficient, has few parameters, and bears little risk of overfitting when e.g.
learning the PCA matrix. Overall, the new compact global descriptor improves
the state-of-the-art on four common benchmarks considerably.
