---
layout: publication
title: "Central Similarity Quantization for Efficient Image and Video Retrieval"
authors: Li Yuan, Tao Wang, Xiaopeng Zhang, Francis EH Tay, Zequn Jie, Wei Liu, Jiashi Feng
conference: CVPR
year: 2020
bibkey: yuan2020quant
additional_links:
   - {name: "PDF", url: "https://openaccess.thecvf.com/content_CVPR_2020/papers/Yuan_Central_Similarity_Quantization_for_Efficient_Image_and_Video_Retrieval_CVPR_2020_paper.pdf"}
   - {name: "Supplementary", url: "https://openaccess.thecvf.com/content_CVPR_2020/supplemental/Yuan_Central_Similarity_Quantization_CVPR_2020_supplemental.pdf"}
   - {name: "Code", url: "https://github.com/yuanli2333/Hadamard-Matrix-for-hashing"}
tags: ["CVPR", "Video Retrieval", "Image Retrieval", "Hash Code", "Deep Learning"]
---
Existing data-dependent hashing methods usually learn hash functions from pairwise or triplet data relationships, which only capture the data similarity locally, and often suffer from low learning efficiency and low collision rate. In this work, we propose a new global similarity metric, termed as central similarity, with which the hash codes of similar data pairs are encouraged to approach a common center and those for dissimilar pairs to converge to different centers, to improve hash learning efficiency and retrieval accuracy. We principally formulate the computation of the proposed central similarity metric by introducing a new concept, i.e., hash center that refers to a set of data points scattered in the Hamming space with a sufficient mutual distance between each other. We then provide an efficient method to construct well separated hash centers by leveraging the Hadamard matrix and Bernoulli distributions. Finally, we propose the Central Similarity Quantization (CSQ) that optimizes the central similarity between data points w.r.t. their hash centers instead of optimizing the local similarity. CSQ is generic and applicable to both image and video hashing scenarios. Extensive experiments on large-scale image and video retrieval tasks demonstrate that CSQ can generate cohesive hash codes for similar data pairs and dispersed hash codes for dissimilar pairs, achieving a noticeable boost in retrieval performance, i.e. 3%-20% in mAP over the previous state-of-the-arts.
