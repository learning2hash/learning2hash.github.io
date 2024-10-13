---
layout: publication
title: Tight Bounds For Monotone Minimal Perfect Hashing
authors: Assadi Sepehr, Farach-colton Martin, Kuszmaul William
conference: "Arxiv"
year: 2022
bibkey: assadi2022tight
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2207.10556"}
tags: ['ARXIV', 'Graph', 'Independent']
---
<p>The monotone minimal perfect hash function (MMPHF) problem is the
following indexing problem. Given a set <span class="math inline">\(S=
\{s_1,\ldots,s_n\}\)</span> of <span class="math inline">\(n\)</span>
distinct keys from a universe <span class="math inline">\(U\)</span> of
size <span class="math inline">\(u\)</span>, create a data structure
<span class="math inline">\(DS\)</span> that answers the following
query: [ RankOp(q) = q S qS ~ ] Solutions to the MMPHF problem are in
widespread use in both theory and practice. The best upper bound known
for the problem encodes <span class="math inline">\(DS\)</span> in <span
class="math inline">\(O(n\log\log\log
u)\)</span> bits and performs queries in <span
class="math inline">\(O(\log u)\)</span> time. It has been an open
problem to either improve the space upper bound or to show that this
somewhat odd looking bound is tight. In this paper, we show the latter:
specifically that any data structure (deterministic or randomized) for
monotone minimal perfect hashing of any collection of <span
class="math inline">\(n\)</span> elements from a universe of size <span
class="math inline">\(u\)</span> requires <span
class="math inline">\(\Omega(n \cdot
\log\log\log{u})\)</span> expected bits to answer every query correctly.
We achieve our lower bound by defining a graph <span
class="math inline">\(\mathbf{G}\)</span> where the nodes are the
possible <span class="math inline">\({u \choose n}\)</span> inputs and
where two nodes are adjacent if they cannot share the same <span
class="math inline">\(DS\)</span>. The size of <span
class="math inline">\(DS\)</span> is then lower bounded by the log of
the chromatic number of <span class="math inline">\(\mathbf{G}\)</span>.
Finally, we show that the fractional chromatic number (and hence the
chromatic number) of <span class="math inline">\(\mathbf{G}\)</span> is
lower bounded by <span class="math inline">\(2^{\Omega(n \log\log\log
u)}\)</span>.</p>
