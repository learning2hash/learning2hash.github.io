---
layout: publication
title: Few-shot Semantic Segmentation With Support-induced Graph Convolutional Network
authors: Jie Liu, Yanqi Bao, Wenzhe Yin, Haochen Wang, Yang Gao, Jan-Jakob Sonke,
  Efstratios Gavves
conference: Arxiv
year: 2023
bibkey: liu2023few
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.03194'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Liu et al.
---
Few-shot semantic segmentation (FSS) aims to achieve novel objects
segmentation with only a few annotated samples and has made great progress
recently. Most of the existing FSS models focus on the feature matching between
support and query to tackle FSS. However, the appearance variations between
objects from the same category could be extremely large, leading to unreliable
feature matching and query mask prediction. To this end, we propose a
Support-induced Graph Convolutional Network (SiGCN) to explicitly excavate
latent context structure in query images. Specifically, we propose a
Support-induced Graph Reasoning (SiGR) module to capture salient query object
parts at different semantic levels with a Support-induced GCN. Furthermore, an
instance association (IA) module is designed to capture high-order instance
context from both support and query instances. By integrating the proposed two
modules, SiGCN can learn rich query context representation, and thus being more
robust to appearance variations. Extensive experiments on PASCAL-5i and
COCO-20i demonstrate that our SiGCN achieves state-of-the-art performance.