---
layout: publication
title: A New Unbiased And Efficient Class Of Lsh-based Samplers And Estimators For
  Partition Function Computation In Log-linear Models
authors: Ryan Spring, Anshumali Shrivastava
conference: Arxiv
year: 2017
bibkey: spring2017a
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.05160'}]
tags: ["Efficiency", "Locality-Sensitive-Hashing", "Scalability"]
short_authors: Ryan Spring, Anshumali Shrivastava
---
Log-linear models are arguably the most successful class of graphical models
for large-scale applications because of their simplicity and tractability.
Learning and inference with these models require calculating the partition
function, which is a major bottleneck and intractable for large state spaces.
Importance Sampling (IS) and MCMC-based approaches are lucrative. However, the
condition of having a "good" proposal distribution is often not satisfied in
practice.
  In this paper, we add a new dimension to efficient estimation via sampling.
We propose a new sampling scheme and an unbiased estimator that estimates the
partition function accurately in sub-linear time. Our samples are generated in
near-constant time using locality sensitive hashing (LSH), and so are
correlated and unnormalized. We demonstrate the effectiveness of our proposed
approach by comparing the accuracy and speed of estimating the partition
function against other state-of-the-art estimation techniques including IS and
the efficient variant of Gumbel-Max sampling. With our efficient sampling
scheme, we accurately train real-world language models using only 1-2% of
computations.