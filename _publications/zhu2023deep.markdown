---
layout: publication
title: Deep Metric Multi-view Hashing For Multimedia Retrieval
authors: Jian Zhu, Zhangmin Huang, Xiaohu Ruan, Yu Cui, Yongli Cheng, Lingfang Zeng
conference: 'Findings of the Association for Computational Linguistics: ACL 2023'
year: 2023
bibkey: zhu2023deep
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.06358'}]
tags: ["Distance Metric Learning", "Evaluation", "Hashing Methods"]
short_authors: Zhu et al.
---
Learning the hash representation of multi-view heterogeneous data is an
important task in multimedia retrieval. However, existing methods fail to
effectively fuse the multi-view features and utilize the metric information
provided by the dissimilar samples, leading to limited retrieval precision.
Current methods utilize weighted sum or concatenation to fuse the multi-view
features. We argue that these fusion methods cannot capture the interaction
among different views. Furthermore, these methods ignored the information
provided by the dissimilar samples. We propose a novel deep metric multi-view
hashing (DMMVH) method to address the mentioned problems. Extensive empirical
evidence is presented to show that gate-based fusion is better than typical
methods. We introduce deep metric learning to the multi-view hashing problems,
which can utilize metric information of dissimilar samples. On the
MIR-Flickr25K, MS COCO, and NUS-WIDE, our method outperforms the current
state-of-the-art methods by a large margin (up to 15.28 mean Average Precision
(mAP) improvement).