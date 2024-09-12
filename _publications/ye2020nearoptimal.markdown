---
layout: publication
title: "Unsupervised Few-Bits Semantic Hashing with Implicit Topics Modeling"
authors: Fanghua Ye, Jarana Manotumruksa, Emine Yilmaz
conference: EMNLP
year: 2020
bibkey: ye2020nearoptimal
additional_links:
   - {name: "PDF", url: "https://www.aclweb.org/anthology/2020.findings-emnlp.233.pdf"}
---
Semantic hashing is a powerful paradigm for
representing texts as compact binary hash
codes. The explosion of short text data has
spurred the demand of few-bits hashing. However, the performance of existing semantic
hashing methods cannot be guaranteed when
applied to few-bits hashing because of severe
information loss. In this paper, we present a
simple but effective unsupervised neural generative semantic hashing method with a focus on
few-bits hashing. Our model is built upon variational autoencoder and represents each hash
bit as a Bernoulli variable, which allows the
model to be end-to-end trainable. To address
the issue of information loss, we introduce a
set of auxiliary implicit topic vectors. With
the aid of these topic vectors, the generated
hash codes are not only low-dimensional representations of the original texts but also capture their implicit topics. We conduct comprehensive experiments on four datasets. The results demonstrate that our approach achieves
significant improvements over state-of-the-art
semantic hashing methods in few-bits hashing.
