---
layout: publication
title: 'Fast Locality Sensitive Hashing With Theoretical Guarantee'
authors: Zongyuan Tan, Hongya Wang, Bo Xu, Minjie Luo, Ming Du
conference: "Arxiv"
year: 2023
citations: 0
bibkey: tan2023fast
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2309.15479'}
tags: ['Independent', 'Efficiency', 'Retrieval Models', 'Evaluation', 'Shallow', 'Unimodal', 'Datasets', 'Hashing']
---
Locality-sensitive hashing (LSH) is an effective randomized technique widely
used in many machine learning tasks. The cost of hashing is proportional to
data dimensions, and thus often the performance bottleneck when dimensionality
is high and the number of hash functions involved is large. Surprisingly,
however, little work has been done to improve the efficiency of LSH
computation. In this paper, we design a simple yet efficient LSH scheme, named
FastLSH, under l2 norm. By combining random sampling and random projection,
FastLSH reduces the time complexity from O(n) to O(m) (m<n), where n is the
data dimensionality and m is the number of sampled dimensions. Moreover,
FastLSH has provable LSH property, which distinguishes it from the non-LSH fast
sketches. We conduct comprehensive experiments over a collection of real and
synthetic datasets for the nearest neighbor search task. Experimental results
demonstrate that FastLSH is on par with the state-of-the-arts in terms of
answer quality, space occupation and query efficiency, while enjoying up to 80x
speedup in hash function evaluation. We believe that FastLSH is a promising
alternative to the classic LSH scheme.
