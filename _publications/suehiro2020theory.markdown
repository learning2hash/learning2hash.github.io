---
layout: publication
title: Theory And Algorithms For Shapelet-based Multiple-instance Learning
authors: Daiki Suehiro, Kohei Hatano, Eiji Takimoto, Shuji Yamamoto, Kenichi Bannai,
  Akiko Takeda
conference: Neural Computation
year: 2020
bibkey: suehiro2020theory
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.01130'}]
tags: []
short_authors: Suehiro et al.
---
We propose a new formulation of Multiple-Instance Learning (MIL), in which a
unit of data consists of a set of instances called a bag. The goal is to find a
good classifier of bags based on the similarity with a "shapelet" (or pattern),
where the similarity of a bag with a shapelet is the maximum similarity of
instances in the bag. In previous work, some of the training instances are
chosen as shapelets with no theoretical justification. In our formulation, we
use all possible, and thus infinitely many shapelets, resulting in a richer
class of classifiers. We show that the formulation is tractable, that is, it
can be reduced through Linear Programming Boosting (LPBoost) to Difference of
Convex (DC) programs of finite (actually polynomial) size. Our theoretical
result also gives justification to the heuristics of some of the previous work.
The time complexity of the proposed algorithm highly depends on the size of the
set of all instances in the training sample. To apply to the data containing a
large number of instances, we also propose a heuristic option of the algorithm
without the loss of the theoretical guarantee. Our empirical study demonstrates
that our algorithm uniformly works for Shapelet Learning tasks on time-series
classification and various MIL tasks with comparable accuracy to the existing
methods. Moreover, we show that the proposed heuristics allow us to achieve the
result with reasonable computational time.