---
layout: publication
title: Learning Decorrelated Hashing Codes For Multimodal Retrieval
authors: Tian Dayong
conference: "Arxiv"
year: 2018
bibkey: tian2018learning
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1803.00682"}
tags: ['ARXIV', 'Cross Modal']
---
In social networks heterogeneous multimedia data correlate to each other such as videos and their corresponding tags in YouTube and image-text pairs in Facebook. Nearest neighbor retrieval across multiple modalities on large data sets becomes a hot yet challenging problem. Hashing is expected to be an efficient solution since it represents data as binary codes. As the bit-wise XOR operations can be fast handled the retrieval time is greatly reduced. Few existing multimodal hashing methods consider the correlation among hashing bits. The correlation has negative impact on hashing codes. When the hashing code length becomes longer the retrieval performance improvement becomes slower. In this paper we propose a minimum correlation regularization (MCR) for multimodal hashing. First the sigmoid function is used to embed the data matrices. Then the MCR is applied on the output of sigmoid function. As the output of sigmoid function approximates a binary code matrix the proposed MCR can efficiently decorrelate the hashing codes. Experiments show the superiority of the proposed method becomes greater as the code length increases.
