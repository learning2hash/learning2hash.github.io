---
layout: publication
title: Threshold And Symmetric Functions Over Bitmaps
authors: Owen Kaser, Daniel Lemire
conference: Arxiv
year: 2014
bibkey: kaser2014threshold
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1402.4073'}]
tags: []
short_authors: Owen Kaser, Daniel Lemire
---
Bitmap indexes are routinely used to speed up simple aggregate queries in
databases. Set operations such as intersections, unions and complements can be
represented as logical operations (AND, OR, NOT). However, less is known about
the application of bitmap indexes to more advanced queries. We want to extend
the applicability of bitmap indexes. As a starting point, we consider symmetric
Boolean queries (e.g., threshold functions). For example, we might consider
stores as sets of products, and ask for products that are on sale in 2 to 10
stores. Such symmetric Boolean queries generalize intersection, union, and
T-occurrence queries.
  It may not be immediately obvious to an engineer how to use bitmap indexes
for symmetric Boolean queries. Yet, maybe surprisingly, we find that the best
of our bitmap-based algorithms are competitive with the state-of-the-art
algorithms for important special cases (e.g., MergeOpt, MergeSkip, DivideSkip,
ScanCount). Moreover, unlike the competing algorithms, the result of our
computation is again a bitmap which can be further processed within a bitmap
index.
  We review algorithmic design issues such as the aggregation of many
compressed bitmaps. We conclude with a discussion on other advanced queries
that bitmap indexes might be able to support efficiently.