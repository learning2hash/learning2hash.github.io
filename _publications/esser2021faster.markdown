---
layout: publication
title: A Faster Algorithm For Finding Closest Pairs In Hamming Metric
authors: "Andre Esser, Robert K\xFCbler, Floyd Zweydinger"
conference: Arxiv
year: 2021
citations: 1
bibkey: esser2021faster
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.02597'}]
tags: [Hashing Methods, Evaluation Metrics]
---
We study the Closest Pair Problem in Hamming metric, which asks to find the
pair with the smallest Hamming distance in a collection of binary vectors. We
give a new randomized algorithm for the problem on uniformly random input
outperforming previous approaches whenever the dimension of input points is
small compared to the dataset size. For moderate to large dimensions, our
algorithm matches the time complexity of the previously best-known locality
sensitive hashing based algorithms. Technically our algorithm follows similar
design principles as Dubiner (IEEE Trans. Inf. Theory 2010) and May-Ozerov
(Eurocrypt 2015). Besides improving the time complexity in the aforementioned
areas, we significantly simplify the analysis of these previous works. We give
a modular analysis, which allows us to investigate the performance of the
algorithm also on non-uniform input distributions. Furthermore, we give a proof
of concept implementation of our algorithm which performs well in comparison to
a quadratic search baseline. This is the first step towards answering an open
question raised by May and Ozerov regarding the practicability of algorithms
following these design principles.