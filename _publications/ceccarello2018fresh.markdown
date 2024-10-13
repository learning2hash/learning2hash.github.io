---
layout: publication
title: FRESH Frechet Similarity With Hashing
authors: Ceccarello Matteo, Driemel Anne, Silvestri Francesco
conference: "Proc. of Algorithms and Data Structures Symposium"
year: 2018
bibkey: ceccarello2018fresh
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1809.02350"}
tags: ['Independent']
---
<p>This paper studies the <span class="math inline">\(r\)</span>-range
search problem for curves under the continuous Fr'echet distance: given
a dataset <span class="math inline">\(S\)</span> of <span
class="math inline">\(n\)</span> polygonal curves and a threshold <span
class="math inline">\(r&gt;0\)</span>, construct a data structure that,
for any query curve <span class="math inline">\(q\)</span>, efficiently
returns all entries in <span class="math inline">\(S\)</span> with
distance at most <span class="math inline">\(r\)</span> from <span
class="math inline">\(q\)</span>. We propose FRESH, an approximate and
randomized approach for <span class="math inline">\(r\)</span>-range
search, that leverages on a locality sensitive hashing scheme for
detecting candidate near neighbors of the query curve, and on a
subsequent pruning step based on a cascade of curve simplifications. We
experimentally compare to exact and deterministic solutions, and we show
that high performance can be reached by suitably relaxing precision and
recall.</p>
