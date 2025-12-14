---
layout: publication
title: Sparse, Dense, And Attentional Representations For Text Retrieval
authors: Yi Luan, Jacob Eisenstein, Kristina Toutanova, Michael Collins
conference: Transactions of the Association for Computational Linguistics
year: 2020
bibkey: luan2020sparse
citations: 154
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.00181'}]
tags: [Evaluation, Efficiency, Scalability, Text Retrieval, TACL, ACL]
short_authors: Luan et al.
---
Dual encoders perform retrieval by encoding documents and queries into dense
lowdimensional vectors, scoring each document by its inner product with the
query. We investigate the capacity of this architecture relative to sparse
bag-of-words models and attentional neural networks. Using both theoretical and
empirical analysis, we establish connections between the encoding dimension,
the margin between gold and lower-ranked documents, and the document length,
suggesting limitations in the capacity of fixed-length encodings to support
precise retrieval of long documents. Building on these insights, we propose a
simple neural model that combines the efficiency of dual encoders with some of
the expressiveness of more costly attentional architectures, and explore
sparse-dense hybrids to capitalize on the precision of sparse retrieval. These
models outperform strong alternatives in large-scale retrieval.