---
layout: publication
title: Adaptive Hashing For Fast Similarity Search
authors: Cakir F., Sclaroff
conference: "Arxiv"
year: 2024
bibkey: cakir2024adaptive
additional_links:
  - {name: "Paper", url: "https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Cakir_Adaptive_Hashing_for_ICCV_2015_paper.pdf"}
tags: ['ARXIV', 'Image Retrieval', 'Independent', 'Streaming Data']
---
<p>With the staggering growth in image and video datasets, algorithms
that provide fast similarity search and compact storage are crucial.
Hashing methods that map the data into Hamming space have shown promise;
however, many of these methods employ a batch-learning strategy in which
the computational cost and memory requirements may become intractable
and infeasible with larger and larger datasets. To overcome these
challenges, we propose an online learning algorithm based on stochastic
gradient descent in which the hash functions are updated iteratively
with streaming data. In experiments with three image retrieval
benchmarks, our online algorithm attains retrieval accuracy that is
comparable to competing state-of-the-art batch-learning solutions, while
our formulation is orders of magnitude faster and being online it is
adaptable to the variations of the data. Moreover, our formulation
yields improved retrieval performance over a recently reported online
hashing technique, Online Kernel Hashing.</p>
