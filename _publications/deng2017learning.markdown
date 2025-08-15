---
layout: publication
title: Learning Deep Similarity Models With Focus Ranking For Fabric Image Retrieval
authors: Daiguo Deng, Ruomei Wang, Hefeng Wu, Huayong He, Qi Li, Xiaonan Luo
conference: Image and Vision Computing
year: 2017
bibkey: deng2017learning
citations: 37
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.10211'}]
tags: ["Datasets", "Image Retrieval"]
short_authors: Deng et al.
---
Fabric image retrieval is beneficial to many applications including clothing
searching, online shopping and cloth modeling. Learning pairwise image
similarity is of great importance to an image retrieval task. With the
resurgence of Convolutional Neural Networks (CNNs), recent works have achieved
significant progresses via deep representation learning with metric embedding,
which drives similar examples close to each other in a feature space, and
dissimilar ones apart from each other. In this paper, we propose a novel
embedding method termed focus ranking that can be easily unified into a CNN for
jointly learning image representations and metrics in the context of
fine-grained fabric image retrieval. Focus ranking aims to rank similar
examples higher than all dissimilar ones by penalizing ranking disorders via
the minimization of the overall cost attributed to similar samples being ranked
below dissimilar ones. At the training stage, training samples are organized
into focus ranking units for efficient optimization. We build a large-scale
fabric image retrieval dataset (FIRD) with about 25,000 images of 4,300
fabrics, and test the proposed model on the FIRD dataset. Experimental results
show the superiority of the proposed model over existing metric embedding
models.