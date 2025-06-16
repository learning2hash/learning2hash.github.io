---
layout: publication
title: Fast Binary Embeddings And Quantized Compressed Sensing With Structured Matrices
authors: Huynh Thang, Saab Rayan
conference: Arxiv
year: 2018
citations: 12
bibkey: huynh2018fast
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.08639'}]
tags: [Quantization, Efficient Learning]
---
This paper deals with two related problems, namely distance-preserving binary
embeddings and quantization for compressed sensing . First, we propose fast
methods to replace points from a subset \\(\mathcal\{X\} \subset \mathbb\{R\}^n\\),
associated with the Euclidean metric, with points in the cube \\(\\{\pm 1\\}^m\\) and
we associate the cube with a pseudo-metric that approximates Euclidean distance
among points in \\(\mathcal\{X\}\\). Our methods rely on quantizing fast
Johnson-Lindenstrauss embeddings based on bounded orthonormal systems and
partial circulant ensembles, both of which admit fast transforms. Our
quantization methods utilize noise-shaping, and include Sigma-Delta schemes and
distributed noise-shaping schemes. The resulting approximation errors decay
polynomially and exponentially fast in \\(m\\), depending on the embedding method.
This dramatically outperforms the current decay rates associated with binary
embeddings and Hamming distances. Additionally, it is the first such binary
embedding result that applies to fast Johnson-Lindenstrauss maps while
preserving \\(ℓ₂\\) norms.
  Second, we again consider noise-shaping schemes, albeit this time to quantize
compressed sensing measurements arising from bounded orthonormal ensembles and
partial circulant matrices. We show that these methods yield a reconstruction
error that again decays with the number of measurements (and bits), when using
convex optimization for reconstruction. Specifically, for Sigma-Delta schemes,
the error decays polynomially in the number of measurements, and it decays
exponentially for distributed noise-shaping schemes based on beta encoding.
These results are near optimal and the first of their kind dealing with bounded
orthonormal systems.