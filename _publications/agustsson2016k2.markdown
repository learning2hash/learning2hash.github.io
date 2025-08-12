---
layout: publication
title: K2-means For Fast And Accurate Large Scale Clustering
authors: Eirikur Agustsson, Radu Timofte, Luc van Gool
conference: Arxiv
year: 2016
bibkey: agustsson2016k2
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1605.09299'}]
tags: []
short_authors: Eirikur Agustsson, Radu Timofte, Luc van Gool
---
We propose k^2-means, a new clustering method which efficiently copes with
large numbers of clusters and achieves low energy solutions. k^2-means builds
upon the standard k-means (Lloyd's algorithm) and combines a new strategy to
accelerate the convergence with a new low time complexity divisive
initialization. The accelerated convergence is achieved through only looking at
k_n nearest clusters and using triangle inequality bounds in the assignment
step while the divisive initialization employs an optimal 2-clustering along a
direction. The worst-case time complexity per iteration of our k^2-means is
O(nk_nd+k^2d), where d is the dimension of the n data points and k is the
number of clusters and usually n << k << k_n. Compared to k-means' O(nkd)
complexity, our k^2-means complexity is significantly lower, at the expense of
slightly increasing the memory complexity by O(nk_n+k^2). In our extensive
experiments k^2-means is order(s) of magnitude faster than standard methods in
computing accurate clusterings on several standard datasets and settings with
hundreds of clusters and high dimensional data. Moreover, the proposed divisive
initialization generally leads to clustering energies comparable to those
achieved with the standard k-means++ initialization, while being significantly
faster.