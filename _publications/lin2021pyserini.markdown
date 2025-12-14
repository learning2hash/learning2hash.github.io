---
layout: publication
title: 'Pyserini: An Easy-to-use Python Toolkit To Support Replicable IR Research
  With Sparse And Dense Representations'
authors: Jimmy Lin, Xueguang Ma, Sheng-Chieh Lin, Jheng-Hong Yang, Ronak Pradeep,
  Rodrigo Nogueira
conference: Arxiv
year: 2021
bibkey: lin2021pyserini
citations: 31
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.10073'}]
tags: [Evaluation, Survey Paper]
short_authors: Lin et al.
---
Pyserini is an easy-to-use Python toolkit that supports replicable IR
research by providing effective first-stage retrieval in a multi-stage ranking
architecture. Our toolkit is self-contained as a standard Python package and
comes with queries, relevance judgments, pre-built indexes, and evaluation
scripts for many commonly used IR test collections. We aim to support, out of
the box, the entire research lifecycle of efforts aimed at improving ranking
with modern neural approaches. In particular, Pyserini supports sparse
retrieval (e.g., BM25 scoring using bag-of-words representations), dense
retrieval (e.g., nearest-neighbor search on transformer-encoded
representations), as well as hybrid retrieval that integrates both approaches.
This paper provides an overview of toolkit features and presents empirical
results that illustrate its effectiveness on two popular ranking tasks. We also
describe how our group has built a culture of replicability through shared
norms and tools that enable rigorous automated testing.