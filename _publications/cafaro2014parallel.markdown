---
layout: publication
title: A Parallel Space Saving Algorithm For Frequent Items And The Hurwitz Zeta Distribution
authors: Massimo Cafaro, Marco Pulimeno, Piergiulio Tempesta
conference: Information Sciences
year: 2015
bibkey: cafaro2014parallel
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1401.0702'}]
tags: []
short_authors: Massimo Cafaro, Marco Pulimeno, Piergiulio Tempesta
---
We present a message-passing based parallel version of the Space Saving
algorithm designed to solve the \\(k\\)--majority problem. The algorithm determines
in parallel frequent items, i.e., those whose frequency is greater than a given
threshold, and is therefore useful for iceberg queries and many other different
contexts. We apply our algorithm to the detection of frequent items in both
real and synthetic datasets whose probability distribution functions are a
Hurwitz and a Zipf distribution respectively. Also, we compare its parallel
performances and accuracy against a parallel algorithm recently proposed for
merging summaries derived by the Space Saving or Frequent algorithms.