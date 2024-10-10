---
layout: publication
title: Binary Embeddings With Structured Hashed Projections
authors: Choromanska Anna, Choromanski Krzysztof, Bojarski Mariusz, Jebara Tony, Kumar Sanjiv, Lecun Yann
conference: "Arxiv"
year: 2015
bibkey: choromanska2015binary
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1511.05212"}
tags: ['ARXIV', 'Independent']
---
We consider the hashing mechanism for constructing binary embeddings that involves pseudo-random projections followed by nonlinear (sign function) mappings. The pseudo-random projection is described by a matrix where not all entries are independent random variables but instead a fixed budget of randomness is distributed across the matrix. Such matrices can be efficiently stored in sub-quadratic or even linear space provide reduction in randomness usage (i.e. number of required random values) and very often lead to computational speed ups. We prove several theoretical results showing that projections via various structured matrices followed by nonlinear mappings accurately preserve the angular distance between input high-dimensional vectors. To the best of our knowledge these results are the first that give theoretical ground for the use of general structured matrices in the nonlinear setting. In particular they generalize previous extensions of the Johnson-Lindenstrauss lemma and prove the plausibility of the approach that was so far only heuristically confirmed for some special structured matrices. Consequently we show that many structured matrices can be used as an efficient information compression mechanism. Our findings build a better understanding of certain deep architectures which contain randomly weighted and untrained layers and yet achieve high performance on different learning tasks. We empirically verify our theoretical findings and show the dependence of learning via structured hashed projections on the performance of neural network as well as nearest neighbor classifier.
