---
layout: publication
title: Manhattan Hashing for Large-Scale Image Retrieval
authors: Kong W., Li, Guo
conference: Proceedings of the 35th international ACM SIGIR conference on Research
  and development in information retrieval
year: 2012
bibkey: kong2012manhattan
citations: 105
additional_links: [{name: Paper, url: 'https://cs.nju.edu.cn/lwj/paper/SIGIR12_MH.pdf'}]
tags: ["Hashing Methods", "Image Retrieval", "SIGIR", "Scalability"]
---
Hashing is used to learn binary-code representation for data with
expectation of preserving the neighborhood structure in the original
feature space. Due to its fast query speed and reduced storage
cost, hashing has been widely used for efficient nearest neighbor
search in a large variety of applications like text and image retrieval.
Most existing hashing methods adopt Hamming distance to
measure the similarity (neighborhood) between points in the hashcode
space. However, one problem with Hamming distance is that
it may destroy the neighborhood structure in the original feature
space, which violates the essential goal of hashing. In this paper,
Manhattan hashing (MH), which is based on Manhattan distance, is
proposed to solve the problem of Hamming distance based hashing.
The basic idea of MH is to encode each projected dimension with
multiple bits of natural binary code (NBC), based on which the
Manhattan distance between points in the hashcode space is calculated
for nearest neighbor search. MH can effectively preserve the
neighborhood structure in the data to achieve the goal of hashing.
To the best of our knowledge, this is the first work to adopt Manhattan
distance with NBC for hashing. Experiments on several largescale
image data sets containing up to one million points show that
our MH method can significantly outperform other state-of-the-art
methods.