---
layout: publication
title: Using Parallelism Techniques To Improve Sequential And Multi-core Sorting Performance
authors: Alexandros V Gerbessiotis
conference: Arxiv
year: 2016
bibkey: gerbessiotis2016using
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1608.08648'}]
tags: []
short_authors: Alexandros V Gerbessiotis
---
We propose new sequential sorting operations by adapting techniques and
methods used for designing parallel sorting algorithms. Although the norm is to
parallelize a sequential algorithm to improve performance, we adapt a
contrarian approach: we employ parallel computing techniques to speed up
sequential sorting. Our methods can also work for multi-core sorting with minor
adjustments that do not necessarily require full parallelization of the
original sequential algorithm. The proposed approach leads to the development
of asymptotically efficient deterministic and randomized sorting operations
whose practical sequential and multi-core performance, as witnessed by an
experimental study, matches or surpasses existing optimized sorting algorithm
implementations.
  We utilize parallel sorting techniques such as deterministic regular sampling
and random oversampling. We extend the notion of deterministic regular sampling
into deterministic regular oversampling for sequential and multi-core sorting
and demonstrate its potential. We then show how these techniques can be used
for sequential sorting and also lead to better multi-core sorting algorithm
performance as witnessed by the undertaken experimental study.