---
layout: publication
title: A Family Of Approximation Algorithms For The Maximum Duo-preservation String
  Mapping Problem
authors: "Bart\u0142omiej Dudek, Pawe\u0142 Gawrychowski, Piotr Ostropolski-Nalewaja"
conference: Arxiv
year: 2017
bibkey: dudek2017family
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.02405'}]
tags: ["Evaluation"]
short_authors: "Bart\u0142omiej Dudek, Pawe\u0142 Gawrychowski, Piotr Ostropolski-Nalewaja"
---
In the Maximum Duo-Preservation String Mapping problem we are given two
strings and wish to map the letters of the former to the letters of the latter
so as to maximise the number of duos. A duo is a pair of consecutive letters
that is mapped to a pair of consecutive letters in the same order. This is
complementary to the well-studied Minimum Common String Partition problem,
where the goal is to partition the former string into blocks that can be
permuted and concatenated to obtain the latter string.
  Maximum Duo-Preservation String Mapping is APX-hard. After a series of
improvements, Brubach [WABI 2016] showed a polynomial-time \(3.25\)-approximation
algorithm. Our main contribution is that for any \(\epsilon>0\) there exists a
polynomial-time \((2+\epsilon)\)-approximation algorithm. Similarly to a previous
solution by Boria et al. [CPM 2016], our algorithm uses the local search
technique. However, this is used only after a certain preliminary greedy
procedure, which gives us more structure and makes a more general local search
possible. We complement this with a specialised version of the algorithm that
achieves \(2.67\)-approximation in quadratic time.