---
layout: publication
title: Cross-modal Center Loss
authors: Longlong Jing, Elahe Vahdani, Jiaxing Tan, Yingli Tian
conference: Arxiv
year: 2020
bibkey: jing2020cross
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.03561'}]
tags: ["Datasets", "Multimodal Retrieval", "Tools & Libraries"]
short_authors: Jing et al.
---
Cross-modal retrieval aims to learn discriminative and modal-invariant
features for data from different modalities. Unlike the existing methods which
usually learn from the features extracted by offline networks, in this paper,
we propose an approach to jointly train the components of cross-modal retrieval
framework with metadata, and enable the network to find optimal features. The
proposed end-to-end framework is updated with three loss functions: 1) a novel
cross-modal center loss to eliminate cross-modal discrepancy, 2) cross-entropy
loss to maximize inter-class variations, and 3) mean-square-error loss to
reduce modality variations. In particular, our proposed cross-modal center loss
minimizes the distances of features from objects belonging to the same class
across all modalities. Extensive experiments have been conducted on the
retrieval tasks across multi-modalities, including 2D image, 3D point cloud,
and mesh data. The proposed framework significantly outperforms the
state-of-the-art methods on the ModelNet40 dataset.