---
layout: publication
title: 'Embedded Spectral Descriptors: Learning The Point-wise Correspondence Metric
  Via Siamese Neural Networks'
authors: Zhiyu Sun, Yusen He, Andrey Gritsenko, Amaury Lendasse, Stephen Baek
conference: Arxiv
year: 2017
bibkey: sun2017embedded
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.06368'}]
tags: ["Distance Metric Learning", "Evaluation"]
short_authors: Sun et al.
---
A robust and informative local shape descriptor plays an important role in
mesh registration. In this regard, spectral descriptors that are based on the
spectrum of the Laplace-Beltrami operator have been a popular subject of
research for the last decade due to their advantageous properties, such as
isometry invariance. Despite such, however, spectral descriptors often fail to
give a correct similarity measure for non-isometric cases where the metric
distortion between the models is large. Hence, they are not reliable for
correspondence matching problems when the models are not isometric. In this
paper, it is proposed a method to improve the similarity metric of spectral
descriptors for correspondence matching problems. We embed a spectral shape
descriptor into a different metric space where the Euclidean distance between
the elements directly indicates the geometric dissimilarity. We design and
train a Siamese neural network to find such an embedding, where the embedded
descriptors are promoted to rearrange based on the geometric similarity. We
demonstrate our approach can significantly enhance the performance of the
conventional spectral descriptors by the simple augmentation achieved via the
Siamese neural network in comparison to other state-of-the-art methods.