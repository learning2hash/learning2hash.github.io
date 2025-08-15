---
layout: publication
title: Neighbourhood Preserving Quantisation For LSH
authors: S. Moran, Lavrenko, Osborne
conference: Proceedings of the 36th international ACM SIGIR conference on Research
  and development in information retrieval
year: 2013
bibkey: moran2013neighbourhood
citations: 22
additional_links: [{name: Paper, url: 'http://homepages.inf.ed.ac.uk/miles/papers/sigir13b.pdf'}]
tags: ["Hashing Methods", "Quantization", "SIGIR"]
short_authors: S. Moran, Lavrenko, Osborne
---
We introduce a scheme for optimally allocating multiple bits per hyperplane for Locality Sensitive Hashing (LSH). Existing approaches binarise LSH projections by thresholding at zero yielding a single bit per dimension. We demonstrate that this is a sub-optimal bit allocation approach that can easily destroy the neighbourhood structure in the original feature space. Our proposed method, dubbed Neighbourhood Preserving Quantization (NPQ), assigns multiple bits per hyperplane based upon adaptively learned thresholds. NPQ exploits a pairwise affinity matrix to discretise each dimension such that nearest neighbours in the original feature space fall within the same quantisation thresholds and are therefore assigned identical bits. NPQ is not only applicable to LSH, but can also be applied to any low-dimensional projection scheme. Despite using half the number of hyperplanes, NPQ is shown to improve LSH-based retrieval accuracy by up to 65% compared to the state-of-the-art.