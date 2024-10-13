---
layout: publication
title: Fast Low-rank Representation Based Spatial Pyramid Matching For Image Classification
authors: Peng Xi, Yan Rui, Zhao Bo, Tang Huajin, Yi Zhang
conference: "Knowledge based Systems"
year: 2014
bibkey: peng2014fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1409.5786"}
tags: ['Quantisation', 'Supervised']
---
Spatial Pyramid Matching (SPM) and its variants have achieved a lot of
success in image classification. The main difference among them is their
encoding schemes. For example, ScSPM incorporates Sparse Code (SC) instead of
Vector Quantization (VQ) into the framework of SPM. Although the methods
achieve a higher recognition rate than the traditional SPM, they consume more
time to encode the local descriptors extracted from the image. In this paper,
we propose using Low Rank Representation (LRR) to encode the descriptors under
the framework of SPM. Different from SC, LRR considers the group effect among
data points instead of sparsity. Benefiting from this property, the proposed
method (i.e., LrrSPM) can offer a better performance. To further improve the
generalizability and robustness, we reformulate the rank-minimization problem
as a truncated projection problem. Extensive experimental studies show that
LrrSPM is more efficient than its counterparts (e.g., ScSPM) while achieving
competitive recognition rates on nine image data sets.
