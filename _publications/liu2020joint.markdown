---
layout: publication
title: Joint-modal Distribution-based Similarity Hashing for Large-scale Unsupervised
  Deep Cross-modal Retrieval
authors: Liu et al.
conference: Proceedings of the 43rd International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2020
bibkey: liu2020joint
citations: 148
additional_links: [{name: Paper, url: 'https://dl.acm.org/doi/abs/10.1145/3397271.3401086'}]
tags: [SCALABILITY, Supervised, SIGIR, Multimodal Retrieval, Unsupervised, Hashing
    Methods]
---
Hashing-based cross-modal search which aims to map multiple modality features into binary codes has attracted increasingly attention due to its storage and search efficiency especially in large-scale database retrieval. Recent unsupervised deep cross-modal hashing methods have shown promising results. However, existing approaches typically suffer from two limitations: (1) They usually learn cross-modal similarity information separately or in a redundant fusion manner, which may fail to capture semantic correlations among instances from different modalities sufficiently and effectively. (2) They seldom consider the sampling and weighting schemes for unsupervised cross-modal hashing, resulting in the lack of satisfactory discriminative ability in hash codes. To overcome these limitations, we propose a novel unsupervised deep cross-modal hashing method called Joint-modal Distribution-based Similarity Hashing (JDSH) for large-scale cross-modal retrieval. Firstly, we propose a novel cross-modal joint-training method by constructing a joint-modal similarity matrix to fully preserve the cross-modal semantic correlations among instances. Secondly, we propose a sampling and weighting scheme termed the Distribution-based Similarity Decision and Weighting (DSDW) method for unsupervised cross-modal hashing, which is able to generate more discriminative hash codes by pushing semantic similar instance pairs closer and pulling semantic dissimilar instance pairs apart. The experimental results demonstrate the superiority of JDSH compared with several unsupervised cross-modal hashing methods on two public datasets NUS-WIDE and MIRFlickr.