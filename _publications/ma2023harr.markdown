---
layout: publication
title: 'HARR: Learning Discriminative And High-quality Hash Codes For Image Retrieval'
authors: Zeyu Ma, Siwei Wang, Xiao Luo, Zhonghui Gu, Chong Chen, Jinxing Li, Xian-Sheng
  Hua, Guangming Lu
conference: ACM Transactions on Multimedia Computing, Communications, and Applications
year: 2023
bibkey: ma2023harr
citations: 8
additional_links: [{name: Paper, url: 'https://dl.acm.org/doi/full/10.1145/3627162'}]
tags: ["Compact Codes", "Evaluation", "Hashing Methods", "Image Retrieval", "Quantization", "Scalability", "Supervised", "Unsupervised"]
short_authors: Ma et al.
---
This article studies deep unsupervised hashing, which has attracted increasing attention in large-scale image retrieval. The majority of recent approaches usually reconstruct semantic similarity information, which then guides the hash code learning. However, they still fail to achieve satisfactory performance in reality for two reasons. On the one hand, without accurate supervised information, these methods usually fail to produce independent and robust hash codes with semantics information well preserved, which may hinder effective image retrieval. On the other hand, due to discrete constraints, how to effectively optimize the hashing network in an end-to-end manner with small quantization errors remains a problem. To address these difficulties, we propose a novel unsupervised hashing method called HARR to learn discriminative and high-quality hash codes. To comprehensively explore semantic similarity structure, HARR adopts the Winner-Take-All hash to model the similarity structure. Then similarity-preserving hash codes are learned under the reliable guidance of the reconstructed similarity structure. Additionally, we improve the quality of hash codes by a bit correlation reduction module, which forces the cross-correlation matrix between a batch of hash codes under different augmentations to approach the identity matrix. In this way, the generated hash bits are expected to be invariant to disturbances with minimal redundancy, which can be further interpreted as an instantiation of the information bottleneck principle. Finally, for effective hashing network training, we minimize the cosine distances between real-value network outputs and their binary codes for small quantization errors. Extensive experiments demonstrate the effectiveness of our proposed HARR.