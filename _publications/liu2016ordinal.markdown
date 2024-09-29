---
layout: publication
title: Ordinal Constrained Binary Code Learning For Nearest Neighbor Search
authors: Liu Hong, Ji Rongrong, Wu Yongjian, Huang Feiyue
conference: "Arxiv"
year: 2016
bibkey: liu2016ordinal
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1611.06362"}
tags: ['ARXIV', 'Graph', 'Supervised']
---
Recent years have witnessed extensive attention in binary code learning a.k.a. hashing for nearest neighbor search problems. It has been seen that high45;dimensional data points can be quantized into binary codes to give an efficient similarity approximation via Hamming distance. Among existing schemes ranking45;based hashing is recent promising that targets at preserving ordinal relations of ranking in the Hamming space to minimize retrieval loss. However the size of the ranking tuples which shows the ordinal relations is quadratic or cubic to the size of training samples. By given a large45;scale training data set it is very expensive to embed such ranking tuples in binary code learning. Besides it remains a dificulty to build ranking tuples efficiently for most ranking45;preserving hashing which are deployed over an ordinal graph45;based setting. To handle these problems we propose a novel ranking45;preserving hashing method dubbed Ordinal Constraint Hashing (OCH) which efficiently learns the optimal hashing functions with a graph45;based approximation to embed the ordinal relations. The core idea is to reduce the size of ordinal graph with ordinal constraint projection which preserves the ordinal relations through a small data set (such as clusters or random samples). In particular to learn such hash functions effectively we further relax the discrete constraints and design a specific stochastic gradient decent algorithm for optimization. Experimental results on three large45;scale visual search benchmark datasets i.e. LabelMe Tiny100K and GIST1M show that the proposed OCH method can achieve superior performance over the state45;of45;the45;arts approaches.
