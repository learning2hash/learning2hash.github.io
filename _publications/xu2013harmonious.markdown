---
layout: publication
title: "Harmonious Hashing"
authors: B. Xu, J. Bu, Y. Chen, X. He, D. Cai
conference: IJCAI
year: 2013
bibkey: xu2013harmonious
additional_links:
   - {name: "PDF", url: "http://ijcai.org/papers13/Papers/IJCAI13-269.pdf"}
   - {name: "Code", url: "https://github.com/dengcai78/MatlabFunc/blob/master/ANNS/Hashing/Unsupervised/HamH_learn.m"}
---
Hashing-based fast nearest neighbor search technique
has attracted great attention in both research
and industry areas recently. Many existing hashing
approaches encode data with projection-based hash
functions and represent each projected dimension
by 1-bit. However, the dimensions with high variance
hold large energy or information of data but
treated equivalently as dimensions with low variance,
which leads to a serious information loss. In
this paper, we introduce a novel hashing algorithm
called Harmonious Hashing which aims at learning
hash functions with low information loss. Specifically,
we learn a set of optimized projections to
preserve the maximum cumulative energy and meet
the constraint of equivalent variance on each dimension
as much as possible. In this way, we could
minimize the information loss after binarization.
Despite the extreme simplicity, our method outperforms
superiorly to many state-of-the-art hashing
methods in large-scale and high-dimensional nearest
neighbor search experiments.
