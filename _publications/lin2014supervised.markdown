---
layout: publication
title: "Supervised Hashing Using Graph Cuts and Boosted Decision Trees"
authors: Lin Guosheng, Shen Chunhua, Hengel Anton van den
conference: Arxiv
year: 2014
bibkey: lin2014supervised
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/1408.5574"}
tags: ['ARXIV', 'Graph', 'Image Retrieval', 'Supervised', 'Unsupervised']
---
Embedding image features into a binary Hamming space can improve both the speed and accuracy of large-scale query-by-example image retrieval systems. Supervised hashing aims to map the original features to compact binary codes in a manner which preserves the label-based similarities of the original data. Most existing approaches apply a single form of hash function, and an optimization process which is typically deeply coupled to this specific form. This tight coupling restricts the flexibility of those methods, and can result in complex optimization problems that are difficult to solve. In this work we proffer a flexible yet simple framework that is able to accommodate different types of loss functions and hash functions. The proposed framework allows a number of existing approaches to hashing to be placed in context, and simplifies the development of new problem-specific hashing methods. Our framework decomposes the into two steps: binary code (hash bits) learning, and hash function learning. The first step can typically be formulated as a binary quadratic problem, and the second step can be accomplished by training standard binary classifiers. For solving large-scale binary code inference, we show how to ensure that the binary quadratic problems are submodular such that an efficient graph cut approach can be used. To achieve efficiency as well as efficacy on large-scale high-dimensional data, we propose to use boosted decision trees as the hash functions, which are nonlinear, highly descriptive, and very fast to train and evaluate. Experiments demonstrate that our proposed method significantly outperforms most state-of-the-art methods, especially on high-dimensional data.