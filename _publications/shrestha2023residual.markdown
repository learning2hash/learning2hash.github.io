---
layout: publication
title: Residual Learning For Image Point Descriptors
authors: Rashik Shrestha, Ajad Chhatkuli, Menelaos Kanakis, Luc van Gool
conference: Arxiv
year: 2023
bibkey: shrestha2023residual
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.15471'}]
tags: []
short_authors: Shrestha et al.
---
Local image feature descriptors have had a tremendous impact on the
development and application of computer vision methods. It is therefore
unsurprising that significant efforts are being made for learning-based image
point descriptors. However, the advantage of learned methods over handcrafted
methods in real applications is subtle and more nuanced than expected.
Moreover, handcrafted descriptors such as SIFT and SURF still perform better
point localization in Structure-from-Motion (SfM) compared to many learned
counterparts. In this paper, we propose a very simple and effective approach to
learning local image descriptors by using a hand-crafted detector and
descriptor. Specifically, we choose to learn only the descriptors, supported by
handcrafted descriptors while discarding the point localization head. We
optimize the final descriptor by leveraging the knowledge already present in
the handcrafted descriptor. Such an approach of optimization allows us to
discard learning knowledge already present in non-differentiable functions such
as the hand-crafted descriptors and only learn the residual knowledge in the
main network branch. This offers 50X convergence speed compared to the standard
baseline architecture of SuperPoint while at inference the combined descriptor
provides superior performance over the learned and hand-crafted descriptors.
This is done with minor increase in the computations over the baseline learned
descriptor. Our approach has potential applications in ensemble learning and
learning with non-differentiable functions. We perform experiments in matching,
camera localization and Structure-from-Motion in order to showcase the
advantages of our approach.