---
layout: publication
title: Elastichash Semantic Image Similarity Search By Deep Hashing With Elasticsearch
authors: Korfhage Nikolaus, Mühling Markus, Freisleben Bernd
conference: "The"
year: 2023
bibkey: korfhage2023elastichash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2305.04710"}
tags: ['AAAI', 'Independent']
---
We present ElasticHash, a novel approach for high-quality, efficient, and large-scale semantic image similarity search. It is based on a deep hashing model to learn hash codes for fine-grained image similarity search in natural images and a two-stage method for efficiently searching binary hash codes using Elasticsearch (ES). In the first stage, a coarse search based on short hash codes is performed using multi-index hashing and ES terms lookup of neighboring hash codes. In the second stage, the list of results is re-ranked by computing the Hamming distance on long hash codes. We evaluate the retrieval performance of \textit\\{ElasticHash\\} for more than 120,000 query images on about 6.9 million database images of the OpenImages data set. The results show that our approach achieves high-quality retrieval results and low search latencies.
