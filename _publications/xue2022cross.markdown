---
layout: publication
title: Cross-Scale Context Extracted Hashing for Fine-Grained Image Binary Encoding
authors: Xue et al.
conference: Arxiv
year: 2022
bibkey: xue2022cross
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.07572'}]
tags: [Hashing Methods]
---
Deep hashing has been widely applied to large-scale image retrieval tasks
owing to efficient computation and low storage cost by encoding
high-dimensional image data into binary codes. Since binary codes do not
contain as much information as float features, the essence of binary encoding
is preserving the main context to guarantee retrieval quality. However, the
existing hashing methods have great limitations on suppressing redundant
background information and accurately encoding from Euclidean space to Hamming
space by a simple sign function. In order to solve these problems, a
Cross-Scale Context Extracted Hashing Network (CSCE-Net) is proposed in this
paper. Firstly, we design a two-branch framework to capture fine-grained local
information while maintaining high-level global semantic information. Besides,
Attention guided Information Extraction module (AIE) is introduced between two
branches, which suppresses areas of low context information cooperated with
global sliding windows. Unlike previous methods, our CSCE-Net learns a
content-related Dynamic Sign Function (DSF) to replace the original simple sign
function. Therefore, the proposed CSCE-Net is context-sensitive and able to
perform well on accurate image binary encoding. We further demonstrate that our
CSCE-Net is superior to the existing hashing methods, which improves retrieval
performance on standard benchmarks.