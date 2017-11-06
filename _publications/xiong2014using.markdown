---
layout: publication
title: "Adaptive Quantization for Hashing:
An Information-Based Approach to Learning Binary Codes"
authors: C. Xiong, W. Chen, G. Chen, D. Johnson, J. Corso
conference: SDM
year: 2014
bibkey: xiong2014using
additional_links:
   - {name: "PDF", url: "https://www.cse.buffalo.edu//~jcorso/pubs/cxiong_SDM2014_adahash.pdf"}
   - {name: "Code", url: "http://www.cse.buffalo.edu/~jcorso/pubs/AQH.zip"}
---
Large-scale data mining and retrieval applications have
increasingly turned to compact binary data representations
as a way to achieve both fast queries and efficient
data storage; many algorithms have been proposed for
learning effective binary encodings. Most of these algorithms
focus on learning a set of projection hyperplanes
for the data and simply binarizing the result from each
hyperplane, but this neglects the fact that informativeness
may not be uniformly distributed across the projections.
In this paper, we address this issue by proposing
a novel adaptive quantization (AQ) strategy that
adaptively assigns varying numbers of bits to different
hyperplanes based on their information content. Our
method provides an information-based schema that preserves
the neighborhood structure of data points, and
we jointly find the globally optimal bit-allocation for
all hyperplanes. In our experiments, we compare with
state-of-the-art methods on four large-scale datasets
and find that our adaptive quantization approach significantly
improves on traditional hashing methods.
