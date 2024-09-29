---
layout: publication
title: Supervised Incremental Hashing
authors: Ozdemir Bahadir, Najibi Mahyar, Davis Larry S.
conference: "Arxiv"
year: 2016
bibkey: ozdemir2016supervised
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1604.07342"}
tags: ['ARXIV', 'Supervised']
---
We propose an incremental strategy for learning hash functions with kernels for large45;scale image search. Our method is based on a two45;stage classification framework that treats binary codes as intermediate variables between the feature space and the semantic space. In the first stage of classification binary codes are considered as class labels by a set of binary SVMs; each corresponds to one bit. In the second stage binary codes become the input space of a multi45;class SVM. Hash functions are learned by an efficient algorithm where the NP45;hard problem of finding optimal binary codes is solved via cyclic coordinate descent and SVMs are trained in a parallelized incremental manner. For modifications like adding images from a previously unseen class we describe an incremental procedure for effective and efficient updates to the previous hash functions. Experiments on three large45;scale image datasets demonstrate the effectiveness of the proposed hashing method Supervised Incremental Hashing (SIH) over the state45;of45;the45;art supervised hashing methods.
