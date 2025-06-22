---
layout: publication
title: 'QUINT: Node Embedding Using Network Hashing'
authors: Debajyoti Bera, Rameshwar Pratap, Bhisham Dev Verma, Biswadeep Sen, Tanmoy
  Chakraborty
conference: Arxiv
year: 2021
citations: 4
bibkey: bera2021node
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.04206'}]
tags: [Tools and Libraries, Efficient Learning, Hashing Methods]
---
Representation learning using network embedding has received tremendous
attention due to its efficacy to solve downstream tasks. Popular embedding
methods (such as deepwalk, node2vec, LINE) are based on a neural architecture,
thus unable to scale on large networks both in terms of time and space usage.
Recently, we proposed BinSketch, a sketching technique for compressing binary
vectors to binary vectors. In this paper, we show how to extend BinSketch and
use it for network hashing. Our proposal named QUINT is built upon BinSketch,
and it embeds nodes of a sparse network onto a low-dimensional space using
simple bi-wise operations. QUINT is the first of its kind that provides
tremendous gain in terms of speed and space usage without compromising much on
the accuracy of the downstream tasks. Extensive experiments are conducted to
compare QUINT with seven state-of-the-art network embedding methods for two end
tasks - link prediction and node classification. We observe huge performance
gain for QUINT in terms of speedup (up to 7000x) and space saving (up to 80x)
due to its bit-wise nature to obtain node embedding. Moreover, QUINT is a
consistent top-performer for both the tasks among the baselines across all the
datasets. Our empirical observations are backed by rigorous theoretical
analysis to justify the effectiveness of QUINT. In particular, we prove that
QUINT retains enough structural information which can be used further to
approximate many topological properties of networks with high confidence.