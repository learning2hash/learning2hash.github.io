---
layout: publication
title: Convolutional Sparse Coding With Overlapping Group Norms
authors: Brendt Wohlberg
conference: Arxiv
year: 2017
bibkey: wohlberg2017convolutional
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.09038'}]
tags: []
short_authors: Brendt Wohlberg
---
The most widely used form of convolutional sparse coding uses an \(\ell_1\)
regularization term. While this approach has been successful in a variety of
applications, a limitation of the \(\ell_1\) penalty is that it is homogeneous
across the spatial and filter index dimensions of the sparse representation
array, so that sparsity cannot be separately controlled across these
dimensions. The present paper considers the consequences of replacing the
\(\ell_1\) penalty with a mixed group norm, motivated by recent theoretical
results for convolutional sparse representations. Algorithms are developed for
solving the resulting problems, which are quite challenging, and the impact on
the performance of the denoising problem is evaluated. The mixed group norms
are found to perform very poorly in this application. While their performance
is greatly improved by introducing a weighting strategy, such a strategy also
improves the performance obtained from the much simpler and computationally
cheaper \(\ell_1\) norm.