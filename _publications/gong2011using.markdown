---
layout: publication
title: "Iterative Quantization: A Procrustean Approach to Learning Binary Codes"
authors: Y. Gong, S. Lazebnik
conference: CVPR
year: 2011
bibkey: gong2011using
additional_links:
   - {name: "PDF", url: "http://slazebni.cs.illinois.edu/publications/cvpr11_small_code.pdf"}
   - {name: "Code", url: "https://github.com/norouzi/ckmeans/blob/master/itq/ITQ.m"}
---
This paper addresses the problem of learning similarity preserving binary codes for efficient retrieval in large-scale image collections. We propose a simple and efficient alternating minimization scheme for finding a rotation of zerocentered data so as to minimize the quantization error of
mapping this data to the vertices of a zero-centered binary
hypercube. This method, dubbed iterative quantization
(ITQ), has connections to multi-class spectral clustering
and to the orthogonal Procrustes problem, and it can be
used both with unsupervised data embeddings such as PCA
and supervised embeddings such as canonical correlation
analysis (CCA). Our experiments show that the resulting
binary coding schemes decisively outperform several other
state-of-the-art methods.
