---
layout: publication
title: Hashing With Binary Autoencoders
authors: M. Carreira-Perpinan, Raziperchikolaei
conference: 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2015
bibkey: carreiraperpinan2015hashing
citations: 142
additional_links: [{name: Paper, url: 'https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Carreira-Perpinan_Hashing_With_Binary_2015_CVPR_paper.pdf'}]
tags: ["CVPR", "Compact Codes", "Hashing Methods", "Image Retrieval"]
short_authors: M. Carreira-Perpinan, Raziperchikolaei
---
An attractive approach for fast search in image
databases is binary hashing, where each high-dimensional,
real-valued image is mapped onto a low-dimensional, binary
vector and the search is done in this binary space.
Finding the optimal hash function is difficult because it involves
binary constraints, and most approaches approximate
the optimization by relaxing the constraints and then
binarizing the result. Here, we focus on the binary autoencoder
model, which seeks to reconstruct an image from the
binary code produced by the hash function. We show that
the optimization can be simplified with the method of auxiliary
coordinates. This reformulates the optimization as
alternating two easier steps: one that learns the encoder
and decoder separately, and one that optimizes the code for
each image. Image retrieval experiments show the resulting
hash function outperforms or is competitive with state-ofthe-art
methods for binary hashing.