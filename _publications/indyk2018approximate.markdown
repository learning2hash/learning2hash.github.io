---
layout: publication
title: Approximate Nearest Neighbors In Limited Space
authors: Indyk Piotr, Wagner Tal
conference: "Arxiv"
year: 2018
bibkey: indyk2018approximate
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1807.00112"}
tags: ['ARXIV', 'Independent']
---
<p>We consider the <span
class="math inline">\((1+\epsilon)\)</span>-approximate nearest neighbor
search problem: given a set <span class="math inline">\(X\)</span> of
<span class="math inline">\(n\)</span> points in a <span
class="math inline">\(d\)</span>-dimensional space, build a data
structure that, given any query point <span
class="math inline">\(y\)</span>, finds a point <span
class="math inline">\(x \in X\)</span> whose distance to <span
class="math inline">\(y\)</span> is at most <span
class="math inline">\((1+\epsilon) \min_{x \in X} \|x-y\|\)</span> for
an accuracy parameter <span class="math inline">\(\epsilon \in
(0,1)\)</span>. Our main result is a data structure that occupies only
<span class="math inline">\(O(\epsilon^{-2} n \log(n)
\log(1/\epsilon))\)</span> bits of space, assuming all point coordinates
are integers in the range <span class="math inline">\(\{-n^{O(1)} \ldots
n^{O(1)}\}\)</span>, i.e., the coordinates have <span
class="math inline">\(O(\log n)\)</span> bits of precision. This
improves over the best previously known space bound of <span
class="math inline">\(O(\epsilon^{-2} n
\log(n)^2)\)</span>, obtained via the randomized dimensionality
reduction method of Johnson and Lindenstrauss (1984). We also consider
the more general problem of estimating all distances from a collection
of query points to all data points <span
class="math inline">\(X\)</span>, and provide almost tight upper and
lower bounds for the space complexity of this problem.</p>
