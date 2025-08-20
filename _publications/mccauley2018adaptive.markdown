---
layout: publication
title: Adaptive Mapreduce Similarity Joins
authors: Samuel McCauley, Francesco Silvestri
conference: Proceedings of the 5th ACM SIGMOD Workshop on Algorithms and Systems for
  MapReduce and Beyond
year: 2018
bibkey: mccauley2018adaptive
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.05615'}]
tags: [Hashing Methods, Locality Sensitive Hashing, Datasets, Evaluation]
short_authors: Samuel McCauley, Francesco Silvestri
---
Similarity joins are a fundamental database operation. Given data sets S and
R, the goal of a similarity join is to find all points x in S and y in R with
distance at most r. Recent research has investigated how locality-sensitive
hashing (LSH) can be used for similarity join, and in particular two recent
lines of work have made exciting progress on LSH-based join performance. Hu,
Tao, and Yi (PODS 17) investigated joins in a massively parallel setting,
showing strong results that adapt to the size of the output. Meanwhile, Ahle,
Aum\"uller, and Pagh (SODA 17) showed a sequential algorithm that adapts to the
structure of the data, matching classic bounds in the worst case but improving
them significantly on more structured data. We show that this adaptive strategy
can be adapted to the parallel setting, combining the advantages of these
approaches. In particular, we show that a simple modification to Hu et al.'s
algorithm achieves bounds that depend on the density of points in the dataset
as well as the total outsize of the output. Our algorithm uses no extra
parameters over other LSH approaches (in particular, its execution does not
depend on the structure of the dataset), and is likely to be efficient in
practice.