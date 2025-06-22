---
layout: publication
title: Multiple Code Hashing For Efficient Image Retrieval
authors: Ming-wei Li, Qing-yuan Jiang, Wu-jun Li
conference: Arxiv
year: 2020
citations: 0
bibkey: li2020multiple
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.01503'}]
tags: [Applications, ANN Search, Hashing Methods, Has Code]
---
Due to its low storage cost and fast query speed, hashing has been widely
used in large-scale image retrieval tasks. Hash bucket search returns data
points within a given Hamming radius to each query, which can enable search at
a constant or sub-linear time cost. However, existing hashing methods cannot
achieve satisfactory retrieval performance for hash bucket search in complex
scenarios, since they learn only one hash code for each image. More
specifically, by using one hash code to represent one image, existing methods
might fail to put similar image pairs to the buckets with a small Hamming
distance to the query when the semantic information of images is complex. As a
result, a large number of hash buckets need to be visited for retrieving
similar images, based on the learned codes. This will deteriorate the
efficiency of hash bucket search. In this paper, we propose a novel hashing
framework, called multiple code hashing (MCH), to improve the performance of
hash bucket search. The main idea of MCH is to learn multiple hash codes for
each image, with each code representing a different region of the image.
Furthermore, we propose a deep reinforcement learning algorithm to learn the
parameters in MCH. To the best of our knowledge, this is the first work that
proposes to learn multiple hash codes for each image in image retrieval.
Experiments demonstrate that MCH can achieve a significant improvement in hash
bucket search, compared with existing methods that learn only one hash code for
each image.