---
layout: publication
title: "Learning to Hash with Binary Reconstructive Embeddings"
authors: B. Kulis, T. Darrell
conference: NIPS
year: 2009
bibkey: kulis2009learning
additional_links:
   - {name: "PDF", url: "https://papers.nips.cc/paper/3667-learning-to-hash-with-binary-reconstructive-embeddings.pdf"}
   - {name: "Code", url: "https://github.com/dengcai78/MatlabFunc/blob/master/ANNS/Hashing/Unsupervised/BRE.m"}
---
Fast retrieval methods are increasingly critical for many large-scale analysis tasks, and there have been
several recent methods that attempt to learn hash functions for fast and accurate nearest neighbor searches.
In this paper, we develop an algorithm for learning hash functions based on explicitly minimizing the
reconstruction error between the original distances and the Hamming distances of the corresponding binary
embeddings. We develop a scalable coordinate-descent algorithm for our proposed hashing objective that
is able to efficiently learn hash functions in a variety of settings. Unlike existing methods such as semantic
hashing and spectral hashing, our method is easily kernelized and does not require restrictive assumptions
about the underlying distribution of the data. We present results over several domains to demonstrate that
our method outperforms existing state-of-the-art techniques.
