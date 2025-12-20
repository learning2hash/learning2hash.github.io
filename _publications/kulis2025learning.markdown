---
layout: publication
title: Learning To Hash With Binary Reconstructive Embeddings
authors: B. Kulis, Darrell
conference: No Venue
year: 2025
bibkey: kulis2025learning
citations: 807
additional_links: [{name: Paper, url: 'https://papers.nips.cc/paper/3667-learning-to-hash-with-binary-reconstructive-embeddings.pdf'}]
tags: ["Efficiency", "Hashing Methods", "Neural Hashing", "Scalability"]
short_authors: B. Kulis, Darrell
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