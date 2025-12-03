---
layout: publication
title: Linear Self-attention Approximation Via Trainable Feedforward Kernel
authors: Uladzislau Yorsh, Alexander Kovalenko
conference: Lecture Notes in Computer Science
year: 2022
bibkey: yorsh2022linear
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.04076'}]
tags: ["Hashing Methods", "Locality-Sensitive-Hashing"]
short_authors: Uladzislau Yorsh, Alexander Kovalenko
---
In pursuit of faster computation, Efficient Transformers demonstrate an
impressive variety of approaches -- models attaining sub-quadratic attention
complexity can utilize a notion of sparsity or a low-rank approximation of
inputs to reduce the number of attended keys; other ways to reduce complexity
include locality-sensitive hashing, key pooling, additional memory to store
information in compacted or hybridization with other architectures, such as
CNN. Often based on a strong mathematical basis, kernelized approaches allow
for the approximation of attention with linear complexity while retaining high
accuracy. Therefore, in the present paper, we aim to expand the idea of
trainable kernel methods to approximate the self-attention mechanism of the
Transformer architecture.