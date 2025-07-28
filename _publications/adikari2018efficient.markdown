---
layout: publication
title: Efficient Learning Of Neighbor Representations For Boundary Trees And Forests
authors: Tharindu Adikari, Stark C. Draper
conference: Arxiv
year: 2018
bibkey: adikari2018efficient
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.11165'}]
tags: []
short_authors: Tharindu Adikari, Stark C. Draper
---
We introduce a semiparametric approach to neighbor-based classification. We
build off the recently proposed Boundary Trees algorithm by Mathy et al.(2015)
which enables fast neighbor-based classification, regression and retrieval in
large datasets. While boundary trees use an Euclidean measure of similarity,
the Differentiable Boundary Tree algorithm by Zoran et al.(2017) was introduced
to learn low-dimensional representations of complex input data, on which
semantic similarity can be calculated to train boundary trees. As is pointed
out by its authors, the differentiable boundary tree approach contains a few
limitations that prevents it from scaling to large datasets. In this paper, we
introduce Differentiable Boundary Sets, an algorithm that overcomes the
computational issues of the differentiable boundary tree scheme and also
improves its classification accuracy and data representability. Our algorithm
is efficiently implementable with existing tools and offers a significant
reduction in training time. We test and compare the algorithms on the well
known MNIST handwritten digits dataset and the newer Fashion-MNIST dataset by
Xiao et al.(2017).