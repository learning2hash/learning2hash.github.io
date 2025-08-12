---
layout: publication
title: Fast Approximations To Structured Sparse Coding And Applications To Object
  Classification
authors: Arthur Szlam, Karol Gregor, Yann Lecun
conference: Lecture Notes in Computer Science
year: 2012
bibkey: szlam2012fast
citations: 42
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1202.6384'}]
tags: []
short_authors: Arthur Szlam, Karol Gregor, Yann Lecun
---
We describe a method for fast approximation of sparse coding. The input space
is subdivided by a binary decision tree, and we simultaneously learn a
dictionary and assignment of allowed dictionary elements for each leaf of the
tree. We store a lookup table with the assignments and the pseudoinverses for
each node, allowing for very fast inference. We give an algorithm for learning
the tree, the dictionary and the dictionary element assignment, and In the
process of describing this algorithm, we discuss the more general problem of
learning the groups in group structured sparse modelling. We show that our
method creates good sparse representations by using it in the object
recognition framework of \cite\{lazebnik06,yang-cvpr-09\}. Implementing our own
fast version of the SIFT descriptor the whole system runs at 20 frames per
second on \(321 \times 481\) sized images on a laptop with a quad-core cpu, while
sacrificing very little accuracy on the Caltech 101 and 15 scenes benchmarks.