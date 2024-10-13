---
layout: publication
title: Locality-sensitive Hashing Without False Negatives For L_p
authors: Pacuk Andrzej, Sankowski Piotr, Wegrzycki Karol, Wygocki Piotr
conference: "Computing and Combinatorics -"
year: 2016
bibkey: pacuk2016locality
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1611.09317"}
tags: ['Independent']
---
<p>In this paper, we show a construction of locality-sensitive hash
functions without false negatives, i.e., which ensure collision for
every pair of points within a given radius <span
class="math inline">\(R\)</span> in <span
class="math inline">\(d\)</span> dimensional space equipped with <span
class="math inline">\(l_p\)</span> norm when <span
class="math inline">\(p \in [1,\infty]\)</span>. Furthermore, we show
how to use these hash functions to solve the <span
class="math inline">\(c\)</span>-approximate nearest neighbor search
problem without false negatives. Namely, if there is a point at distance
<span class="math inline">\(R\)</span>, we will certainly report it and
points at distance greater than <span class="math inline">\(cR\)</span>
will not be reported for <span
class="math inline">\(c=\Omega(\sqrt{d},d^{1-\frac{1}{p}})\)</span>. The
constructed algorithms work: - with preprocessing time <span
class="math inline">\(\mathcal{O}(n \log(n))\)</span> and sublinear
expected query time, - with preprocessing time <span
class="math inline">\(\mathcal{O}(\mathrm{poly}(n))\)</span> and
expected query time <span
class="math inline">\(\mathcal{O}(\log(n))\)</span>. Our paper reports
progress on answering the open problem presented by Pagh [8] who
considered the nearest neighbor search without false negatives for the
Hamming distance.</p>
