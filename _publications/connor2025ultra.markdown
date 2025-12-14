---
layout: publication
title: 'Ultra-quantisation: Efficient Embedding Search Via 1.58-bit Encodings'
authors: Richard Connor, Alan Dearle, Ben Claydon
conference: Arxiv
year: 2025
bibkey: connor2025ultra
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.00528'}]
tags: [Evaluation, Quantization]
short_authors: Richard Connor, Alan Dearle, Ben Claydon
---
Many modern search domains comprise high-dimensional vectors of floating point numbers derived from neural networks, in the form of embeddings. Typical embeddings range in size from hundreds to thousands of dimensions, making the size of the embeddings, and the speed of comparison, a significant issue.
  Quantisation is a class of mechanism which replaces the floating point values with a smaller representation, for example a short integer. This gives an approximation of the embedding space in return for a smaller data representation and a faster comparison function.
  Here we take this idea almost to its extreme: we show how vectors of arbitrary-precision floating point values can be replaced by vectors whose elements are drawn from the set \{-1,0,1\}. This yields very significant savings in space and metric evaluation cost, while maintaining a strong correlation for similarity measurements.
  This is achieved by way of a class of convex polytopes which exist in the high-dimensional space. In this article we give an outline description of these objects, and show how they can be used for the basis of such radical quantisation while maintaining a surprising degree of accuracy.