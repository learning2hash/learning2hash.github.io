---
layout: publication
title: Deep Triplet Hashing Network For Case45;based Medical Image Retrieval
authors: Fang Jiansheng, Fu Huazhu, Liu Jiang
conference: "Arxiv"
year: 2021
bibkey: fang2021deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2101.12346"}
tags: ['ARXIV', 'Image Retrieval', 'Supervised']
---
Deep hashing methods have been shown to be the most efficient approximate nearest neighbor search techniques for large45;scale image retrieval. However existing deep hashing methods have a poor small45;sample ranking performance for case45;based medical image retrieval. The top45;ranked images in the returned query results may be as a different class than the query image. This ranking problem is caused by classification regions of interest (ROI) and small45;sample information loss in the hashing space. To address the ranking problem we propose an end45;to45;end framework called Attention45;based Triplet Hashing (ATH) network to learn low45;dimensional hash codes that preserve the classification ROI and small45;sample information. We embed a spatial45;attention module into the network structure of our ATH to focus on ROI information. The spatial45;attention module aggregates the spatial information of feature maps by utilizing max45;pooling element45;wise maximum and element45;wise mean operations jointly along the channel axis. The triplet cross45;entropy loss can help to map the classification information of images and similarity between images into the hash codes. Extensive experiments on two case45;based medical datasets demonstrate that our proposed ATH can further improve the retrieval performance compared to the state45;of45;the45;art deep hashing methods and boost the ranking performance for small samples. Compared to the other loss methods the triplet cross45;entropy loss can enhance the classification performance and hash code45;discriminability
