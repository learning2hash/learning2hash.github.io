---
layout: publication
title: Efficient Similarity Search In Dynamic Data Streams
authors: Marc Bury, Chris Schwiegelshohn, Mara Sorella
conference: Arxiv
year: 2016
citations: 0
bibkey: bury2016efficient
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1605.03949'}]
tags: [Tools and Libraries, Hashing Methods]
---
The Jaccard index is an important similarity measure for item sets and
Boolean data. On large datasets, an exact similarity computation is often
infeasible for all item pairs both due to time and space constraints, giving
rise to faster approximate methods. The algorithm of choice used to quickly
compute the Jaccard index \\(\frac\{\vert A \cap B \vert\}\{\vert A\cup B\vert\}\\) of
two item sets \\(A\\) and \\(B\\) is usually a form of min-hashing. Most min-hashing
schemes are maintainable in data streams processing only additions, but none
are known to work when facing item-wise deletions. In this paper, we
investigate scalable approximation algorithms for rational set similarities, a
broad class of similarity measures including Jaccard. Motivated by a result of
Chierichetti and Kumar [J. ACM 2015] who showed any rational set similarity \\(S\\)
admits a locality sensitive hashing (LSH) scheme if and only if the
corresponding distance \\(1-S\\) is a metric, we can show that there exists a space
efficient summary maintaining a \\((1\pm \epsilon)\\) multiplicative
approximation to \\(1-S\\) in dynamic data streams. This in turn also yields a
\\(\epsilon\\) additive approximation of the similarity. The existence of these
approximations hints at, but does not directly imply a LSH scheme in dynamic
data streams. Our second and main contribution now lies in the design of such a
LSH scheme maintainable in dynamic data streams. The scheme is space efficient,
easy to implement and to the best of our knowledge the first of its kind able
to process deletions.