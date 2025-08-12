---
layout: publication
title: Instance Adaptive Prototypical Contrastive Embedding For Generalized Zero Shot
  Learning
authors: Riti Paul, Sahil Vora, Baoxin Li
conference: Arxiv
year: 2023
bibkey: paul2023instance
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.06987'}]
tags: ["Distance Metric Learning", "Few Shot & Zero Shot"]
short_authors: Riti Paul, Sahil Vora, Baoxin Li
---
Generalized zero-shot learning(GZSL) aims to classify samples from seen and
unseen labels, assuming unseen labels are not accessible during training.
Recent advancements in GZSL have been expedited by incorporating
contrastive-learning-based (instance-based) embedding in generative networks
and leveraging the semantic relationship between data points. However, existing
embedding architectures suffer from two limitations: (1) limited
discriminability of synthetic features' embedding without considering
fine-grained cluster structures; (2) inflexible optimization due to restricted
scaling mechanisms on existing contrastive embedding networks, leading to
overlapped representations in the embedding space. To enhance the quality of
representations in the embedding space, as mentioned in (1), we propose a
margin-based prototypical contrastive learning embedding network that reaps the
benefits of prototype-data (cluster quality enhancement) and implicit data-data
(fine-grained representations) interaction while providing substantial cluster
supervision to the embedding network and the generator. To tackle (2), we
propose an instance adaptive contrastive loss that leads to generalized
representations for unseen labels with increased inter-class margin. Through
comprehensive experimental evaluation, we show that our method can outperform
the current state-of-the-art on three benchmark datasets. Our approach also
consistently achieves the best unseen performance in the GZSL setting.