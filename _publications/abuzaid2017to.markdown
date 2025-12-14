---
layout: publication
title: 'To Index Or Not To Index: Optimizing Exact Maximum Inner Product Search'
authors: Firas Abuzaid, Geet Sethi, Peter Bailis, Matei Zaharia
conference: Arxiv
year: 2017
bibkey: abuzaid2017to
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.01449'}]
tags: [Evaluation, Similarity Search, Efficiency, Datasets, Recommender Systems]
short_authors: Abuzaid et al.
---
Exact Maximum Inner Product Search (MIPS) is an important task that is widely
pertinent to recommender systems and high-dimensional similarity search. The
brute-force approach to solving exact MIPS is computationally expensive, thus
spurring recent development of novel indexes and pruning techniques for this
task. In this paper, we show that a hardware-efficient brute-force approach,
blocked matrix multiply (BMM), can outperform the state-of-the-art MIPS solvers
by over an order of magnitude, for some -- but not all -- inputs.
  In this paper, we also present a novel MIPS solution, MAXIMUS, that takes
advantage of hardware efficiency and pruning of the search space. Like BMM,
MAXIMUS is faster than other solvers by up to an order of magnitude, but again
only for some inputs. Since no single solution offers the best runtime
performance for all inputs, we introduce a new data-dependent optimizer,
OPTIMUS, that selects online with minimal overhead the best MIPS solver for a
given input. Together, OPTIMUS and MAXIMUS outperform state-of-the-art MIPS
solvers by 3.2\(\times\) on average, and up to 10.9\(\times\), on widely studied
MIPS datasets.