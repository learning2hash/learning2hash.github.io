---
layout: publication
title: Multiple-instance Learning By Boosting Infinitely Many Shapelet-based Classifiers
authors: Daiki Suehiro, Kohei Hatano, Eiji Takimoto, Shuji Yamamoto, Kenichi Bannai,
  Akiko Takeda
conference: Arxiv
year: 2018
bibkey: suehiro2018multiple
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.08084'}]
tags: []
short_authors: Suehiro et al.
---
We propose a new formulation of Multiple-Instance Learning (MIL). In typical
MIL settings, a unit of data is given as a set of instances called a bag and
the goal is to find a good classifier of bags based on similarity from a single
or finitely many "shapelets" (or patterns), where the similarity of the bag
from a shapelet is the maximum similarity of instances in the bag. Classifiers
based on a single shapelet are not sufficiently strong for certain
applications. Additionally, previous work with multiple shapelets has
heuristically chosen some of the instances as shapelets with no theoretical
guarantee of its generalization ability. Our formulation provides a richer
class of the final classifiers based on infinitely many shapelets. We provide
an efficient algorithm for the new formulation, in addition to generalization
bound. Our empirical study demonstrates that our approach is effective not only
for MIL tasks but also for Shapelet Learning for time-series classification.