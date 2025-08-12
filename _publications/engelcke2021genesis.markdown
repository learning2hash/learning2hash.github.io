---
layout: publication
title: 'GENESIS-V2: Inferring Unordered Object Representations Without Iterative Refinement'
authors: Martin Engelcke, Oiwi Parker Jones, Ingmar Posner
conference: Arxiv
year: 2021
bibkey: engelcke2021genesis
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.09958'}]
tags: ["Unsupervised"]
short_authors: Martin Engelcke, Oiwi Parker Jones, Ingmar Posner
---
Advances in unsupervised learning of object-representations have culminated
in the development of a broad range of methods for unsupervised object
segmentation and interpretable object-centric scene generation. These methods,
however, are limited to simulated and real-world datasets with limited visual
complexity. Moreover, object representations are often inferred using RNNs
which do not scale well to large images or iterative refinement which avoids
imposing an unnatural ordering on objects in an image but requires the a priori
initialisation of a fixed number of object representations. In contrast to
established paradigms, this work proposes an embedding-based approach in which
embeddings of pixels are clustered in a differentiable fashion using a
stochastic stick-breaking process. Similar to iterative refinement, this
clustering procedure also leads to randomly ordered object representations, but
without the need of initialising a fixed number of clusters a priori. This is
used to develop a new model, GENESIS-v2, which can infer a variable number of
object representations without using RNNs or iterative refinement. We show that
GENESIS-v2 performs strongly in comparison to recent baselines in terms of
unsupervised image segmentation and object-centric scene generation on
established synthetic datasets as well as more complex real-world datasets.