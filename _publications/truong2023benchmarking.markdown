---
layout: publication
title: Benchmarking Pretrained Vision Embeddings For Near- And Duplicate Detection
  In Medical Images
authors: Truong Tuan, Jush Farnaz Khun, Lenga Matthias
conference: 2024 IEEE International Symposium on Biomedical Imaging (ISBI)
year: 2024
bibkey: truong2023benchmarking
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.07273'}]
tags: ["Self-Supervised", "Vector-Indexing", "Similarity-Search", "Datasets", "Supervised", "Evaluation"]
short_authors: Truong Tuan, Jush Farnaz Khun, Lenga Matthias
---
Near- and duplicate image detection is a critical concern in the field of
medical imaging. Medical datasets often contain similar or duplicate images
from various sources, which can lead to significant performance issues and
evaluation biases, especially in machine learning tasks due to data leakage
between training and testing subsets. In this paper, we present an approach for
identifying near- and duplicate 3D medical images leveraging publicly available
2D computer vision embeddings. We assessed our approach by comparing embeddings
extracted from two state-of-the-art self-supervised pretrained models and two
different vector index structures for similarity retrieval. We generate an
experimental benchmark based on the publicly available Medical Segmentation
Decathlon dataset. The proposed method yields promising results for near- and
duplicate image detection achieving a mean sensitivity and specificity of
0.9645 and 0.8559, respectively.