---
layout: publication
title: Bagminhash - Minwise Hashing Algorithm For Weighted Sets
authors: Otmar Ertl
conference: Proceedings of the 24th ACM SIGKDD International Conference on Knowledge
  Discovery &amp; Data Mining
year: 2018
bibkey: ertl2018bagminhash
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.03914'}]
tags: [Hashing Methods, KDD]
short_authors: Otmar Ertl
---
Minwise hashing has become a standard tool to calculate signatures which
allow direct estimation of Jaccard similarities. While very efficient
algorithms already exist for the unweighted case, the calculation of signatures
for weighted sets is still a time consuming task. BagMinHash is a new algorithm
that can be orders of magnitude faster than current state of the art without
any particular restrictions or assumptions on weights or data dimensionality.
Applied to the special case of unweighted sets, it represents the first
efficient algorithm producing independent signature components. A series of
tests finally verifies the new algorithm and also reveals limitations of other
approaches published in the recent past.