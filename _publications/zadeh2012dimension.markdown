---
layout: publication
title: Dimension Independent Similarity Computation
authors: Reza Bosagh Zadeh, Ashish Goel
conference: Arxiv
year: 2013
bibkey: zadeh2012dimension
citations: 53
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1206.2082'}]
tags: [Locality Sensitive Hashing, Tools & Libraries]
short_authors: Reza Bosagh Zadeh, Ashish Goel
---
We present a suite of algorithms for Dimension Independent Similarity
Computation (DISCO) to compute all pairwise similarities between very high
dimensional sparse vectors. All of our results are provably independent of
dimension, meaning apart from the initial cost of trivially reading in the
data, all subsequent operations are independent of the dimension, thus the
dimension can be very large. We study Cosine, Dice, Overlap, and the Jaccard
similarity measures. For Jaccard similiarity we include an improved version of
MinHash. Our results are geared toward the MapReduce framework. We empirically
validate our theorems at large scale using data from the social networking site
Twitter. At time of writing, our algorithms are live in production at
twitter.com.