---
layout: publication
title: Neural Similarity Learning
authors: Weiyang Liu, Zhen Liu, James M. Rehg, Le Song
conference: Arxiv
year: 2019
bibkey: liu2019neural
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.13003'}]
tags: ["Evaluation"]
short_authors: Liu et al.
---
Inner product-based convolution has been the founding stone of convolutional
neural networks (CNNs), enabling end-to-end learning of visual representation.
By generalizing inner product with a bilinear matrix, we propose the neural
similarity which serves as a learnable parametric similarity measure for CNNs.
Neural similarity naturally generalizes the convolution and enhances
flexibility. Further, we consider the neural similarity learning (NSL) in order
to learn the neural similarity adaptively from training data. Specifically, we
propose two different ways of learning the neural similarity: static NSL and
dynamic NSL. Interestingly, dynamic neural similarity makes the CNN become a
dynamic inference network. By regularizing the bilinear matrix, NSL can be
viewed as learning the shape of kernel and the similarity measure
simultaneously. We further justify the effectiveness of NSL with a theoretical
viewpoint. Most importantly, NSL shows promising performance in visual
recognition and few-shot learning, validating the superiority of NSL over the
inner product-based convolution counterparts.