---
layout: publication
title: Angular Quantization-based Binary Codes For Fast Similarity Search
authors: Yunchao Gong, Sanjiv Kumar, Vishal Verma, Svetlana Lazebnik
conference: "Neural Information Processing Systems"
year: 2012
citations: 103
bibkey: gong2012angular
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2012/hash/f5deaeeae1538fb6c45901d524ee2f98-Abstract.html"}
tags: ['NEURIPS', 'Quantisation', 'Text Retrieval']
---
This paper focuses on the problem of learning binary embeddings for efficient retrieval of high-dimensional non-negative data. Such data typically arises in a large number of vision and text applications where counts or frequencies are used as features.  Also, cosine distance is commonly used as a measure of dissimilarity between such vectors. In this work, we introduce a novel spherical quantization scheme to generate binary embedding of such data and analyze its properties. The number of quantization landmarks in this scheme grows exponentially with data dimensionality resulting in low-distortion quantization.  We propose a very efficient method for computing the binary embedding using such large number of landmarks. Further, a linear transformation is learned to minimize the quantization error by adapting the method to the input data resulting in improved embedding.  Experiments on image and text retrieval applications show superior performance of the proposed method over other existing state-of-the-art methods.
