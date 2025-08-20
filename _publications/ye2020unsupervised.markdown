---
layout: publication
title: Unsupervised Few-bits Semantic Hashing With Implicit Topics Modeling
authors: Fanghua Ye, Manotumruksa, Yilmaz
conference: 'Findings of the Association for Computational Linguistics: EMNLP 2020'
year: 2020
bibkey: ye2020unsupervised
citations: 4
additional_links: [{name: Paper, url: 'https://www.aclweb.org/anthology/2020.findings-emnlp.233.pdf'}]
tags: [Hashing Methods, Datasets, ACL, EMNLP, Unsupervised, Evaluation, Neural Hashing]
short_authors: Fanghua Ye, Manotumruksa, Yilmaz
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