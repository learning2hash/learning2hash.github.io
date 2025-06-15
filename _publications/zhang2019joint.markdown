---
layout: publication
title: 'Joint Cluster Unary Loss For Efficient Cross-modal Hashing'
authors: Shifeng Zhang, Jianmin Li, Bo Zhang
conference: "Arxiv"
year: 2019
citations: 4
bibkey: zhang2019joint
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1902.00644'}
tags: ['Hashing Methods', 'Loss Functions', 'Modality-Specific Hashing', 'Tools and Libraries', 'Hashing Fundamentals', 'Learning Strategies', 'Multi-Modal Hashing']
---
With the rapid growth of various types of multimodal data, cross-modal deep
hashing has received broad attention for solving cross-modal retrieval problems
efficiently. Most cross-modal hashing methods follow the traditional supervised
hashing framework in which the \\(O(n^2)\\) data pairs and \\(O(n^3)\\) data triplets
are generated for training, but the training procedure is less efficient
because the complexity is high for large-scale dataset. To address these
issues, we propose a novel and efficient cross-modal hashing algorithm in which
the unary loss is introduced. First of all, We introduce the Cross-Modal Unary
Loss (CMUL) with \\(O(n)\\) complexity to bridge the traditional triplet loss and
classification-based unary loss. A more accurate bound of the triplet loss for
structured multilabel data is also proposed in CMUL. Second, we propose the
novel Joint Cluster Cross-Modal Hashing (JCCH) algorithm for efficient hash
learning, in which the CMUL is involved. The resultant hashcodes form several
clusters in which the hashcodes in the same cluster share similar semantic
information, and the heterogeneity gap on different modalities is diminished by
sharing the clusters. The proposed algorithm is able to be applied to various
types of data, and experiments on large-scale datasets show that the proposed
method is superior over or comparable with state-of-the-art cross-modal hashing
methods, and training with the proposed method is more efficient than others.
