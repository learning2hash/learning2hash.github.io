---
layout: publication
title: Efficient Similarity Search In Dynamic Data Streams
authors: Bury Marc, Schwiegelshohn Chris, Sorella Mara
conference: "Arxiv"
year: 2016
bibkey: bury2016efficient
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1605.03949"}
tags: ['ARXIV', 'Independent', 'LSH']
---
<p>The Jaccard index is an important similarity measure for item sets
and Boolean data. On large datasets, an exact similarity computation is
often infeasible for all item pairs both due to time and space
constraints, giving rise to faster approximate methods. The algorithm of
choice used to quickly compute the Jaccard index <span
class="math inline">\(\frac{\vert A \cap B \vert}{\vert A\cup
B\vert}\)</span> of two item sets <span class="math inline">\(A\)</span>
and <span class="math inline">\(B\)</span> is usually a form of
min-hashing. Most min-hashing schemes are maintainable in data streams
processing only additions, but none are known to work when facing
item-wise deletions. In this paper, we investigate scalable
approximation algorithms for rational set similarities, a broad class of
similarity measures including Jaccard. Motivated by a result of
Chierichetti and Kumar [J. ACM 2015] who showed any rational set
similarity <span class="math inline">\(S\)</span> admits a locality
sensitive hashing (LSH) scheme if and only if the corresponding distance
<span class="math inline">\(1-S\)</span> is a metric, we can show that
there exists a space efficient summary maintaining a <span
class="math inline">\((1\pm \varepsilon)\)</span> multiplicative
approximation to <span class="math inline">\(1-S\)</span> in dynamic
data streams. This in turn also yields a <span
class="math inline">\(\varepsilon\)</span> additive approximation of the
similarity. The existence of these approximations hints at, but does not
directly imply a LSH scheme in dynamic data streams. Our second and main
contribution now lies in the design of such a LSH scheme maintainable in
dynamic data streams. The scheme is space efficient, easy to implement
and to the best of our knowledge the first of its kind able to process
deletions.</p>
