---
layout: publication
title: Large-margin Representation Learning For Texture Classification
authors: Jonathan de Matos, Luiz Eduardo Soares de Oliveira, Alceu de Souza Britto
  Junior, Alessandro Lameiras Koerich
conference: Pattern Recognition Letters
year: 2023
bibkey: dematos2022large
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.08537'}]
tags: ["Distance Metric Learning"]
short_authors: Matos et al.
---
This paper presents a novel approach combining convolutional layers (CLs) and
large-margin metric learning for training supervised models on small datasets
for texture classification. The core of such an approach is a loss function
that computes the distances between instances of interest and support vectors.
The objective is to update the weights of CLs iteratively to learn a
representation with a large margin between classes. Each iteration results in a
large-margin discriminant model represented by support vectors based on such a
representation. The advantage of the proposed approach w.r.t. convolutional
neural networks (CNNs) is two-fold. First, it allows representation learning
with a small amount of data due to the reduced number of parameters compared to
an equivalent CNN. Second, it has a low training cost since the backpropagation
considers only support vectors. The experimental results on texture and
histopathologic image datasets have shown that the proposed approach achieves
competitive accuracy with lower computational cost and faster convergence when
compared to equivalent CNNs.