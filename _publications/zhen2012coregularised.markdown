---
layout: publication
title: "Co-Regularized Hashing for Multimodal Data"
authors: Y. Zhen, D. Yeung
conference: NIPS
year: 2012
bibkey: zhen2012coregularised
additional_links:
   - {name: "PDF", url: "http://papers.nips.cc/paper/4793-co-regularized-hashing-for-multimodal-data.pdf"}
---
Hashing-based methods provide a very promising approach to large-scale similarity
search. To obtain compact hash codes, a recent trend seeks to learn the hash
functions from data automatically. In this paper, we study hash function learning
in the context of multimodal data. We propose a novel multimodal hash function
learning method, called Co-Regularized Hashing (CRH), based on a boosted coregularization
framework. The hash functions for each bit of the hash codes are
learned by solving DC (difference of convex functions) programs, while the learning
for multiple bits proceeds via a boosting procedure so that the bias introduced
by the hash functions can be sequentially minimized. We empirically compare
CRH with two state-of-the-art multimodal hash function learning methods on two
publicly available data sets.
