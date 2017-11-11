---
layout: publication
title: "Locality-sensitive binary codes from shift-invariant kernels"
authors: M. Raginsky, S. Lazebnik
conference: NIPS
year: 2009
bibkey: raginsky2009locality
additional_links:
   - {name: "PDF", url: "http://papers.nips.cc/paper/3749-locality-sensitive-binary-codes-from-shift-invariant-kernels.pdf"}
   - {name: "Code", url: "http://www.unc.edu/~yunchao/code/smallcode.zip"}
   - {name: "Talk", url: "https://www.robots.ox.ac.uk/~vgg/rg/slides/binarycodes.pdf"}
---
This paper addresses the problem of designing binary codes for high-dimensional
data such that vectors that are similar in the original space map to similar binary
strings. We introduce a simple distribution-free encoding scheme based on
random projections, such that the expected Hamming distance between the binary
codes of two vectors is related to the value of a shift-invariant kernel (e.g., a
Gaussian kernel) between the vectors. We present a full theoretical analysis of the
convergence properties of the proposed scheme, and report favorable experimental
performance as compared to a recent state-of-the-art method, spectral hashing.
