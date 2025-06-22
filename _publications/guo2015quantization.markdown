---
layout: publication
title: Quantization Based Fast Inner Product Search
authors: Ruiqi Guo, Sanjiv Kumar, Krzysztof Choromanski, David Simcha
conference: Arxiv
year: 2015
citations: 57
bibkey: guo2015quantization
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1509.01469'}]
tags: [Quantization, ANN Search, Has Code]
---
We propose a quantization based approach for fast approximate Maximum Inner
Product Search (MIPS). Each database vector is quantized in multiple subspaces
via a set of codebooks, learned directly by minimizing the inner product
quantization error. Then, the inner product of a query to a database vector is
approximated as the sum of inner products with the subspace quantizers.
Different from recently proposed LSH approaches to MIPS, the database vectors
and queries do not need to be augmented in a higher dimensional feature space.
We also provide a theoretical analysis of the proposed approach, consisting of
the concentration results under mild assumptions. Furthermore, if a small
sample of example queries is given at the training time, we propose a modified
codebook learning procedure which further improves the accuracy. Experimental
results on a variety of datasets including those arising from deep neural
networks show that the proposed approach significantly outperforms the existing
state-of-the-art.