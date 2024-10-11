---
layout: publication
title: Unsupervised Feature Learning For Dense Correspondences Across Scenes
authors: Zhang Chao, Shen Chunhua, Shen Tingzhi
conference: "Arxiv"
year: 2015
bibkey: zhang2015unsupervised
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1501.00642"}
tags: ['ARXIV', 'Unsupervised']
---
We propose a fast, accurate matching method for estimating dense pixel correspondences across scenes. It is a challenging problem to estimate dense pixel correspondences between images depicting different scenes or instances of the same object category. While most such matching methods rely on hand-crafted features such as SIFT, we learn features from a large amount of unlabeled image patches using unsupervised learning. Pixel-layer features are obtained by encoding over the dictionary, followed by spatial pooling to obtain patch-layer features. The learned features are then seamlessly embedded into a multi-layer match- ing framework. We experimentally demonstrate that the learned features, together with our matching model, outperforms state-of-the-art methods such as the SIFT flow, coherency sensitive hashing and the recent deformable spatial pyramid matching methods both in terms of accuracy and computation efficiency. Furthermore, we evaluate the performance of a few different dictionary learning and feature encoding methods in the proposed pixel correspondences estimation framework, and analyse the impact of dictionary learning and feature encoding with respect to the final matching performance.
