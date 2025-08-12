---
layout: publication
title: Multi-similarity Based Hyperrelation Network For Few-shot Segmentation
authors: Xiangwen Shi, Zhe Cui, Shaobing Zhang, Miao Cheng, Lian He, Xianghong Tang
conference: IET Image Processing
year: 2022
bibkey: shi2022multi
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.09550'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Shi et al.
---
Few-shot semantic segmentation aims at recognizing the object regions of
unseen categories with only a few annotated examples as supervision. The key to
few-shot segmentation is to establish a robust semantic relationship between
the support and query images and to prevent overfitting. In this paper, we
propose an effective Multi-similarity Hyperrelation Network (MSHNet) to tackle
the few-shot semantic segmentation problem. In MSHNet, we propose a new
Generative Prototype Similarity (GPS), which together with cosine similarity
can establish a strong semantic relation between the support and query images.
The locally generated prototype similarity based on global feature is logically
complementary to the global cosine similarity based on local feature, and the
relationship between the query image and the supported image can be expressed
more comprehensively by using the two similarities simultaneously. In addition,
we propose a Symmetric Merging Block (SMB) in MSHNet to efficiently merge
multi-layer, multi-shot and multi-similarity hyperrelational features. MSHNet
is built on the basis of similarity rather than specific category features,
which can achieve more general unity and effectively reduce overfitting. On two
benchmark semantic segmentation datasets Pascal-5i and COCO-20i, MSHNet
achieves new state-of-the-art performances on 1-shot and 5-shot semantic
segmentation tasks.