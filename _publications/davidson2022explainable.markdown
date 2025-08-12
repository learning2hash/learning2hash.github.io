---
layout: publication
title: 'Explainable Clustering Via Exemplars: Complexity And Efficient Approximation
  Algorithms'
authors: Ian Davidson, Michael Livanos, Antoine Gourru, Peter Walker, Julien Velcin,
  S. S. Ravi
conference: Arxiv
year: 2022
bibkey: davidson2022explainable
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.09670'}]
tags: ["Evaluation"]
short_authors: Davidson et al.
---
Explainable AI (XAI) is an important developing area but remains relatively
understudied for clustering. We propose an explainable-by-design clustering
approach that not only finds clusters but also exemplars to explain each
cluster. The use of exemplars for understanding is supported by the
exemplar-based school of concept definition in psychology. We show that finding
a small set of exemplars to explain even a single cluster is computationally
intractable; hence, the overall problem is challenging. We develop an
approximation algorithm that provides provable performance guarantees with
respect to clustering quality as well as the number of exemplars used. This
basic algorithm explains all the instances in every cluster whilst another
approximation algorithm uses a bounded number of exemplars to allow simpler
explanations and provably covers a large fraction of all the instances.
Experimental results show that our work is useful in domains involving
difficult to understand deep embeddings of images and text.