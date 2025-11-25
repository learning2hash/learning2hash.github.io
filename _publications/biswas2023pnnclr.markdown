---
layout: publication
title: 'Pnnclr: Stochastic Pseudo Neighborhoods For Contrastive Learning Based Unsupervised
  Representation Learning Problems'
authors: Momojit Biswas, Himanshu Buckchash, Dilip K. Prasad
conference: Arxiv
year: 2023
bibkey: biswas2023pnnclr
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.06983'}]
tags: ["Distance Metric Learning", "Self-Supervised", "Unsupervised"]
short_authors: Momojit Biswas, Himanshu Buckchash, Dilip K. Prasad
---
Nearest neighbor (NN) sampling provides more semantic variations than
pre-defined transformations for self-supervised learning (SSL) based image
recognition problems. However, its performance is restricted by the quality of
the support set, which holds positive samples for the contrastive loss. In this
work, we show that the quality of the support set plays a crucial role in any
nearest neighbor based method for SSL. We then provide a refined baseline
(pNNCLR) to the nearest neighbor based SSL approach (NNCLR). To this end, we
introduce pseudo nearest neighbors (pNN) to control the quality of the support
set, wherein, rather than sampling the nearest neighbors, we sample in the
vicinity of hard nearest neighbors by varying the magnitude of the resultant
vector and employing a stochastic sampling strategy to improve the performance.
Additionally, to stabilize the effects of uncertainty in NN-based learning, we
employ a smooth-weight-update approach for training the proposed network.
Evaluation of the proposed method on multiple public image recognition and
medical image recognition datasets shows that it performs up to 8 percent
better than the baseline nearest neighbor method, and is comparable to other
previously proposed SSL methods.