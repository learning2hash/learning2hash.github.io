---
layout: publication
title: Distribution Aligned Feature Clustering For Zero-shot Sketch-based Image Retrieval
authors: Yuchen Wu, Kun Song, Fangzheng Zhao, Jiansheng Chen, Huimin Ma
conference: Arxiv
year: 2023
bibkey: wu2023distribution
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.06685'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Wu et al.
---
Zero-Shot Sketch-Based Image Retrieval (ZS-SBIR) is a challenging cross-modal
retrieval task. In prior arts, the retrieval is conducted by sorting the
distance between the query sketch and each image in the gallery. However, the
domain gap and the zero-shot setting make neural networks hard to generalize.
This paper tackles the challenges from a new perspective: utilizing gallery
image features. We propose a Cluster-then-Retrieve (ClusterRetri) method that
performs clustering on the gallery images and uses the cluster centroids as
proxies for retrieval. Furthermore, a distribution alignment loss is proposed
to align the image and sketch features with a common Gaussian distribution,
reducing the domain gap. Despite its simplicity, our proposed method
outperforms the state-of-the-art methods by a large margin on popular datasets,
e.g., up to 31% and 39% relative improvement of mAP@all on the Sketchy and
TU-Berlin datasets.