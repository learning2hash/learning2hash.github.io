---
layout: publication
title: Informative Sample-aware Proxy For Deep Metric Learning
authors: Aoyu Li, Ikuro Sato, Kohta Ishikawa, Rei Kawakami, Rio Yokota
conference: Proceedings of the 4th ACM International Conference on Multimedia in Asia
year: 2022
bibkey: li2022informative
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.10382'}]
tags: [Distance Metric Learning, Datasets, Supervised]
short_authors: Li et al.
---
Among various supervised deep metric learning methods proxy-based approaches
have achieved high retrieval accuracies. Proxies, which are
class-representative points in an embedding space, receive updates based on
proxy-sample similarities in a similar manner to sample representations. In
existing methods, a relatively small number of samples can produce large
gradient magnitudes (ie, hard samples), and a relatively large number of
samples can produce small gradient magnitudes (ie, easy samples); these can
play a major part in updates. Assuming that acquiring too much sensitivity to
such extreme sets of samples would deteriorate the generalizability of a
method, we propose a novel proxy-based method called Informative Sample-Aware
Proxy (Proxy-ISA), which directly modifies a gradient weighting factor for each
sample using a scheduled threshold function, so that the model is more
sensitive to the informative samples. Extensive experiments on the
CUB-200-2011, Cars-196, Stanford Online Products and In-shop Clothes Retrieval
datasets demonstrate the superiority of Proxy-ISA compared with the
state-of-the-art methods.