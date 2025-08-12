---
layout: publication
title: Enhancing Histograms By Tree-like Bucket Indices
authors: Francesco Buccafurri, Gianluca Lax, Domenico Sacca', Luigi Pontieri, Domenico
  Rosaci
conference: The VLDB Journal
year: 2007
bibkey: buccafurri2005enhancing
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/cs/0501020'}]
tags: ["Tree Based ANN"]
short_authors: Buccafurri et al.
---
Histograms are used to summarize the contents of relations into a number of
buckets for the estimation of query result sizes. Several techniques (e.g.,
MaxDiff and V-Optimal) have been proposed in the past for determining bucket
boundaries which provide accurate estimations. However, while search strategies
for optimal bucket boundaries are rather sophisticated, no much attention has
been paid for estimating queries inside buckets and all of the above techniques
adopt naive methods for such an estimation. This paper focuses on the problem
of improving the estimation inside a bucket once its boundaries have been
fixed. The proposed technique is based on the addition, to each bucket, of
32-bit additional information (organized into a 4-level tree index), storing
approximate cumulative frequencies at 7 internal intervals of the bucket. Both
theoretical analysis and experimental results show that, among a number of
alternative ways to organize the additional information, the 4-level tree index
provides the best frequency estimation inside a bucket. The index is later
added to two well-known histograms, MaxDiff and V-Optimal, obtaining the
non-obvious result that despite the spatial cost of 4LT which reduces the
number of allowed buckets once the storage space has been fixed, the original
methods are strongly improved in terms of accuracy.