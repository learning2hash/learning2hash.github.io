---
layout: publication
title: Balanced Allocations And Double Hashing
authors: Mitzenmacher Michael
conference: "Arxiv"
year: 2012
bibkey: mitzenmacher2012balanced
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1209.5360"}
tags: ['ARXIV', 'Independent']
---
<p>Double hashing has recently found more common usage in schemes that
use multiple hash functions. In double hashing, for an item <span
class="math inline">\(x\)</span>, one generates two hash values <span
class="math inline">\(f(x)\)</span> and <span
class="math inline">\(g(x)\)</span>, and then uses combinations <span
class="math inline">\((f(x) +k g(x)) \bmod
n\)</span> for <span class="math inline">\(k=0,1,2,...\)</span> to
generate multiple hash values from the initial two. We first perform an
empirical study showing that, surprisingly, the performance difference
between double hashing and fully random hashing appears negligible in
the standard balanced allocation paradigm, where each item is placed in
the least loaded of <span class="math inline">\(d\)</span> choices, as
well as several related variants. We then provide theoretical results
that explain the behavior of double hashing in this context.</p>
