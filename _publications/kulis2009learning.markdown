---
layout: publication
title: Learning To Hash With Binary Reconstructive Embeddings
authors: Brian Kulis, Trevor Darrell
conference: Neural Information Processing Systems
year: 2009
citations: 841
bibkey: kulis2009learning
additional_links: [{name: Paper, url: 'https://papers.nips.cc/paper/2009/hash/6602294be910b1e3c4571bd98c4d5484-Abstract.html'}]
tags: [Hashing Methods, ANN Search, Efficient Learning, NEURIPS]
---
Fast retrieval methods are increasingly critical for many large-scale analysis tasks, and there have been several recent methods that attempt to learn hash functions for fast and accurate nearest neighbor searches.  In this paper, we develop an algorithm for learning hash functions based on explicitly minimizing the reconstruction error between the original distances and the Hamming distances of the corresponding binary embeddings.  We develop a scalable coordinate-descent algorithm for our proposed hashing objective that is able to efficiently learn hash functions in a variety of settings.  Unlike existing methods such as semantic hashing and spectral hashing, our method is easily kernelized and does not require restrictive assumptions about the underlying distribution of the data.  We present results over several domains to demonstrate that our method outperforms existing state-of-the-art techniques.