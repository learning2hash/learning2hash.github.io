---
layout: publication
title: Learning Hash Function Through Codewords
authors: Yinjie Huang, Michael Georgiopoulos, Georgios C. Anagnostopoulos
conference: Arxiv
year: 2019
citations: 0
bibkey: huang2019learning
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.08639'}]
tags: [Hashing Methods, Unsupervised, Supervised, Applications, Has Code]
---
In this paper, we propose a novel hash learning approach that has the
following main distinguishing features, when compared to past frameworks.
First, the codewords are utilized in the Hamming space as ancillary techniques
to accomplish its hash learning task. These codewords, which are inferred from
the data, attempt to capture grouping aspects of the data's hash codes.
Furthermore, the proposed framework is capable of addressing supervised,
unsupervised and, even, semi-supervised hash learning scenarios. Additionally,
the framework adopts a regularization term over the codewords, which
automatically chooses the codewords for the problem. To efficiently solve the
problem, one Block Coordinate Descent algorithm is showcased in the paper. We
also show that one step of the algorithms can be casted into several Support
Vector Machine problems which enables our algorithms to utilize efficient
software package. For the regularization term, a closed form solution of the
proximal operator is provided in the paper. A series of comparative experiments
focused on content-based image retrieval highlights its performance advantages.