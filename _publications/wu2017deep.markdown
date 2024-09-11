---
layout: publication
title: "Deep Supervised Hashing for Multi-Label and Large-Scale Image Retrieval"
authors: Dayan Wu, Zheng Lin, Bo Li, Mingzhen Ye, Weiping Wang
conference: ICMR
year: 2017
bibkey: wu2017deep
additional_links:
   - {name: "PDF", url: "https://dl.acm.org/citation.cfm?id=3078989"}
tags: ["ICMR", "Image Retrieval", "Supervised", "Deep Learning"]
---
One of the most challenging tasks in large-scale multi-label image retrieval is to map images into binary codes while preserving multilevel semantic similarity. Recently, several deep supervised hashing methods have been proposed to learn hash functions that preserve multilevel semantic similarity with deep convolutional neural networks. However, these triplet label based methods try to preserve the ranking order of images according to their similarity degrees to the queries while not putting direct constraints on the distance between the codes of very similar images. Besides, the current evaluation criteria are not able to measure the performance of existing hashing methods on preserving fine-grained multilevel semantic similarity. To tackle these issues, we propose a novel Deep Multilevel Semantic Similarity Preserving Hashing (DMSSPH) method to learn compact similarity-preserving binary codes for the huge body of multi-label image data with deep convolutional neural networks. In our approach, we make the best of the supervised information in the form of pairwise labels to maximize the discriminability of output binary codes. Extensive evaluations conducted on several benchmark datasets demonstrate that the proposed method significantly outperforms the state-of-the-art supervised and unsupervised hashing methods at the accuracies of top returned images, especially for shorter binary codes. Meanwhile, the proposed method shows better performance on preserving fine-grained multilevel semantic similarity according to the results under the Jaccard coefficient based evaluation criteria we propose.
