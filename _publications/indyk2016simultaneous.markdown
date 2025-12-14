---
layout: publication
title: Simultaneous Nearest Neighbor Search
authors: Piotr Indyk, Robert Kleinberg, Sepideh Mahabadi, Yang Yuan
conference: Arxiv
year: 2016
bibkey: indyk2016simultaneous
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.02188'}]
tags: [Uncategorized]
short_authors: Indyk et al.
---
Motivated by applications in computer vision and databases, we introduce and
study the Simultaneous Nearest Neighbor Search (SNN) problem. Given a set of
data points, the goal of SNN is to design a data structure that, given a
collection of queries, finds a collection of close points that are compatible
with each other. Formally, we are given \(k\) query points \(Q=q_1,\cdots,q_k\),
and a compatibility graph \(G\) with vertices in \(Q\), and the goal is to return
data points \(p_1,\cdots,p_k\) that minimize (i) the weighted sum of the
distances from \(q_i\) to \(p_i\) and (ii) the weighted sum, over all edges \((i,j)\)
in the compatibility graph \(G\), of the distances between \(p_i\) and \(p_j\). The
problem has several applications, where one wants to return a set of consistent
answers to multiple related queries. This generalizes well-studied
computational problems, including NN, Aggregate NN and the 0-extension problem.
  In this paper we propose and analyze the following general two-step method
for designing efficient data structures for SNN. In the first step, for each
query point \(q_i\) we find its (approximate) nearest neighbor point \(\hat\{p\}_i\);
this can be done efficiently using existing approximate nearest neighbor
structures. In the second step, we solve an off-line optimization problem over
sets \(q_1,\cdots,q_k\) and \(\hat\{p\}_1,\cdots,\hat\{p\}_k\); this can be done
efficiently given that \(k\) is much smaller than \(n\). Even though
\(\hat\{p\}_1,\cdots,\hat\{p\}_k\) might not constitute the optimal answers to
queries \(q_1,\cdots,q_k\), we show that, for the unweighted case, the resulting
algorithm is \(O(log k/log log k)\)-approximation. Also, we show that the
approximation factor can be in fact reduced to a constant for compatibility
graphs frequently occurring in practice.
  Finally, we show that the "empirical approximation factor" provided by the
above approach is very close to 1.