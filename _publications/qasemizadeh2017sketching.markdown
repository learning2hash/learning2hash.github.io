---
layout: publication
title: Sketching Word Vectors Through Hashing
authors: Behrang Qasemizadeh, Laura Kallmeyer
conference: Arxiv
year: 2017
citations: 4
bibkey: qasemizadeh2017sketching
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.04253'}]
tags: [Hashing Methods]
---
We propose a new fast word embedding technique using hash functions. The
method is a derandomization of a new type of random projections: By
disregarding the classic constraint used in designing random projections (i.e.,
preserving pairwise distances in a particular normed space), our solution
exploits extremely sparse non-negative random projections. Our experiments show
that the proposed method can achieve competitive results, comparable to neural
embedding learning techniques, however, with only a fraction of the
computational complexity of these methods. While the proposed derandomization
enhances the computational and space complexity of our method, the possibility
of applying weighting methods such as positive pointwise mutual information
(PPMI) to our models after their construction (and at a reduced dimensionality)
imparts a high discriminatory power to the resulting embeddings. Obviously,
this method comes with other known benefits of random projection-based
techniques such as ease of update.