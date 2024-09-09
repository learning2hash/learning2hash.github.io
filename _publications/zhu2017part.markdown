---
layout: publication
title: "Part-based Deep Hashing for Large-scale Person Re-identification"
authors: Zhu Fuqing, Kong Xiangwei, Zheng Liang, Fu Haiyan, Tian Qi
conference: Arxiv
year: 2017
bibkey: zhu2017part
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1705.02145"}
tags: ['ARXIV', 'Deep Learning']
---
Large-scale is a trend in person re-identification (re-id). It is important that real-time search be performed in a large gallery. While previous methods mostly focus on discriminative learning, this paper makes the attempt in integrating deep learning and hashing into one framework to evaluate the efficiency and accuracy for large-scale person re-id. We integrate spatial information for discriminative visual representation by partitioning the pedestrian image into horizontal parts. Specifically, Part-based Deep Hashing (PDH) is proposed, in which batches of triplet samples are employed as the input of the deep hashing architecture. Each triplet sample contains two pedestrian images (or parts) with the same identity and one pedestrian image (or part) of the different identity. A triplet loss function is employed with a constraint that the Hamming distance of pedestrian images (or parts) with the same identity is smaller than ones with the different identity. In the experiment, we show that the proposed Part-based Deep Hashing method yields very competitive re-id accuracy on the large-scale Market-1501 and Market-1501+500K datasets.