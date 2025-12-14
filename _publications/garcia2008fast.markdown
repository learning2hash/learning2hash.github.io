---
layout: publication
title: Fast K Nearest Neighbor Search Using GPU
authors: Vincent Garcia, Eric Debreuve, Michel Barlaud
conference: 2008 IEEE Computer Society Conference on Computer Vision and Pattern Recognition
  Workshops
year: 2008
bibkey: garcia2008fast
citations: 440
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/0804.1448'}]
tags: [CVPR, Tools & Libraries]
short_authors: Vincent Garcia, Eric Debreuve, Michel Barlaud
---
The recent improvements of graphics processing units (GPU) offer to the
computer vision community a powerful processing platform. Indeed, a lot of
highly-parallelizable computer vision problems can be significantly accelerated
using GPU architecture. Among these algorithms, the k nearest neighbor search
(KNN) is a well-known problem linked with many applications such as
classification, estimation of statistical properties, etc. The main drawback of
this task lies in its computation burden, as it grows polynomially with the
data size. In this paper, we show that the use of the NVIDIA CUDA API
accelerates the search for the KNN up to a factor of 120.