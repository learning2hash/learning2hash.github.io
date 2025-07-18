---
layout: publication
title: Edge Sampling And Graph Parameter Estimation Via Vertex Neighborhood Accesses
authors: "T\u011Btek Jakub, Thorup Mikkel"
conference: Proceedings of the 54th Annual ACM SIGACT Symposium on Theory of Computing
year: 2021
bibkey: "t\u011Btek2021edge"
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.03821'}]
tags: [Tools & Libraries, Hashing Methods]
---
In this paper, we consider the problems from the area of sublinear-time
algorithms of edge sampling, edge counting, and triangle counting. Part of our
contribution is that we consider three different settings, differing in the way
in which one may access the neighborhood of a given vertex. In previous work,
people have considered indexed neighbor access, with a query returning the
\\(i\\)-th neighbor of a given vertex. Full neighborhood access model, which has a
query that returns the entire neighborhood at a unit cost, has recently been
considered in the applied community. Between these, we propose hash-ordered
neighbor access, inspired by coordinated sampling, where we have a global fully
random hash function, and can access neighbors in order of their hash values,
paying a constant for each accessed neighbor.
  For edge sampling and counting, our new lower bounds are in the most powerful
full neighborhood access model. We provide matching upper bounds in the weaker
hash-ordered neighbor access model. Our new faster algorithms can be provably
implemented efficiently on massive graphs in external memory and with the
current APIs for, e.g., Twitter or Wikipedia. For triangle counting, we provide
a separation: a better upper bound with full neighborhood access than the known
lower bounds with indexed neighbor access. The technical core of our paper is
our edge-sampling algorithm on which the other results depend.