---
layout: publication
title: Sublinear Least-squares Value Iteration Via Locality Sensitive Hashing
authors: Anshumali Shrivastava, Zhao Song, Zhaozhuo Xu
conference: Arxiv
year: 2021
bibkey: shrivastava2021sublinear
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.08285'}]
tags: [Hashing Methods, Locality Sensitive Hashing]
short_authors: Anshumali Shrivastava, Zhao Song, Zhaozhuo Xu
---
We present the first provable Least-Squares Value Iteration (LSVI) algorithms
that have runtime complexity sublinear in the number of actions. We formulate
the value function estimation procedure in value iteration as an approximate
maximum inner product search problem and propose a locality sensitive hashing
(LSH) [Indyk and Motwani STOC'98, Andoni and Razenshteyn STOC'15, Andoni,
Laarhoven, Razenshteyn and Waingarten SODA'17] type data structure to solve
this problem with sublinear time complexity. Moreover, we build the connections
between the theory of approximate maximum inner product search and the regret
analysis of reinforcement learning. We prove that, with our choice of
approximation factor, our Sublinear LSVI algorithms maintain the same regret as
the original LSVI algorithms while reducing the runtime complexity to sublinear
in the number of actions. To the best of our knowledge, this is the first work
that combines LSH with reinforcement learning resulting in provable
improvements. We hope that our novel way of combining data-structures and
iterative algorithm will open the door for further study into cost reduction in
optimization.