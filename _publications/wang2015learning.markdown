---
layout: publication
title: Learning to Hash for Indexing Big Data - A Survey
authors: Wang Jun, Liu Wei, Kumar Sanjiv, Chang Shih-fu
conference: "Arxiv"
year: 2015
bibkey: wang2015learning
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1509.05472"}
tags: ['ARXIV', 'Deep Learning', 'LSH', 'Survey Paper', 'Unsupervised']
---
The explosive growth in big data has attracted much attention in designing efficient indexing and search methods recently. In many critical applications such as large-scale search and pattern matching finding the nearest neighbors to a query is a fundamental research problem. However the straightforward solution using exhaustive comparison is infeasible due to the prohibitive computational complexity and memory requirement. In response Approximate Nearest Neighbor (ANN) search based on hashing techniques has become popular due to its promising performance in both efficiency and accuracy. Prior randomized hashing methods e.g. Locality-Sensitive Hashing (LSH) explore data-independent hash functions with random projections or permutations. Although having elegant theoretic guarantees on the search quality in certain metric spaces performance of randomized hashing has been shown insufficient in many real-world applications. As a remedy new approaches incorporating data-driven learning methods in development of advanced hash functions have emerged. Such learning to hash methods exploit information such as data distributions or class labels when optimizing the hash codes or functions. Importantly the learned hash codes are able to preserve the proximity of neighboring data in the original feature spaces in the hash code spaces. The goal of this paper is to provide readers with systematic understanding of insights pros and cons of the emerging techniques. We provide a comprehensive survey of the learning to hash framework and representative techniques of various types including unsupervised semi-supervised and supervised. In addition we also summarize recent hashing approaches utilizing the deep learning models. Finally we discuss the future direction and trends of research in this area.
