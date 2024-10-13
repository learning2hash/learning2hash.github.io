---
layout: publication
title: Sub-linear Memory Sketches For Near Neighbor Search On Streaming Data
authors: Coleman Benjamin, Baraniuk Richard G., Shrivastava Anshumali
conference: "Arxiv"
year: 2019
bibkey: coleman2019sub
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1902.06687"}
tags: ['ARXIV', 'Independent', 'LSH', 'Streaming Data']
---
<p>We present the first sublinear memory sketch that can be queried to
find the nearest neighbors in a dataset. Our online sketching algorithm
compresses an N element dataset to a sketch of size <span
class="math inline">\(O(N^b \log^3 N)\)</span> in <span
class="math inline">\(O(N^{(b+1)} \log^3
N)\)</span> time, where <span class="math inline">\(b &lt; 1\)</span>.
This sketch can correctly report the nearest neighbors of any query that
satisfies a stability condition parameterized by <span
class="math inline">\(b\)</span>. We achieve sublinear memory
performance on stable queries by combining recent advances in locality
sensitive hash (LSH)-based estimators, online kernel density estimation,
and compressed sensing. Our theoretical results shed new light on the
memory-accuracy tradeoff for nearest neighbor search, and our sketch,
which consists entirely of short integer arrays, has a variety of
attractive features in practice. We evaluate the memory-recall tradeoff
of our method on a friend recommendation task in the Google Plus social
media network. We obtain orders of magnitude better compression than the
random projection based alternative while retaining the ability to
report the nearest neighbors of practical queries.</p>
