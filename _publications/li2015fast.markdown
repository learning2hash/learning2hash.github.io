---
layout: publication
title: "Fast k-Nearest Neighbour Search via Dynamic Continuous Indexing"
authors: Li Ke, Malik Jitendra
conference: Arxiv
year: 2015
bibkey: li2015fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1512.00442"}
tags: ['ARXIV', 'LSH', 'TOM']
---
Existing methods for retrieving k-nearest neighbours suffer from the curse of dimensionality. We argue this is caused in part by inherent deficiencies of space partitioning, which is the underlying strategy used by most existing methods. We devise a new strategy that avoids partitioning the vector space and present a novel randomized algorithm that runs in time linear in dimensionality of the space and sub-linear in the intrinsic dimensionality and the size of the dataset and takes space constant in dimensionality of the space and linear in the size of the dataset. The proposed algorithm allows fine-grained control over accuracy and speed on a per-query basis, automatically adapts to variations in data density, supports dynamic updates to the dataset and is easy-to-implement. We show appealing theoretical properties and demonstrate empirically that the proposed algorithm outperforms locality-sensitivity hashing (LSH) in terms of approximation quality, speed and space efficiency.