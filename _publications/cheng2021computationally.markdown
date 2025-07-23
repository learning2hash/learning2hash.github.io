---
layout: publication
title: Computationally Efficient Learning Of Statistical Manifolds
authors: Cheng Fan, Panagiotelis Anastasios, Hyndman Rob J
conference: Arxiv
year: 2021
bibkey: cheng2021computationally
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.11773'}]
tags: ["Efficiency"]
short_authors: Cheng Fan, Panagiotelis Anastasios, Hyndman Rob J
---
Analyzing high-dimensional data with manifold learning algorithms often
requires searching for the nearest neighbors of all observations. This presents
a computational bottleneck in statistical manifold learning when observations
of probability distributions rather than vector-valued variables are available
or when data size is large. We resolve this problem by proposing a new method
for approximation in statistical manifold learning. The novelty of our
approximation is the strongly consistent distance estimators based on
independent and identically distributed samples from probability distributions.
By exploiting the connection between Hellinger/total variation distance for
discrete distributions and the L2/L1 norm, we demonstrate that the proposed
distance estimators, combined with approximate nearest neighbor searching,
could largely improve the computational efficiency with little to no loss in
the accuracy of manifold embedding. The result is robust to different manifold
learning algorithms and different approximate nearest neighbor algorithms. The
proposed method is applied to learning statistical manifolds of electricity
usage. This application demonstrates how underlying structures in high
dimensional data, including anomalies, can be visualized and identified, in a
way that is scalable to large datasets.