---
layout: publication
title: Coveringlsh Locality-sensitive Hashing Without False Negatives
authors: Pagh Rasmus
conference: "Arxiv"
year: 2015
bibkey: pagh2015coveringlsh
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1507.03225"}
tags: ['ARXIV', 'Independent', 'LSH']
---
<p>We consider a new construction of locality-sensitive hash functions
for Hamming space that is in the sense that is it guaranteed to produce
a collision for every pair of vectors within a given radius <span
class="math inline">\(r\)</span>. The construction is in the sense that
the expected number of hash collisions between vectors at distance~<span
class="math inline">\(cr\)</span>, for a given <span
class="math inline">\(c&gt;1\)</span>, comes close to that of the best
possible data independent LSH without the covering guarantee, namely,
the seminal LSH construction of Indyk and Motwani (STOC ’98). The
efficiency of the new construction essentially their bound when the
search radius is not too large — e.g., when <span
class="math inline">\(cr = o(\log(n)/\log\log n)\)</span>, where <span
class="math inline">\(n\)</span> is the number of points in the data
set, and when <span class="math inline">\(cr = \log(n)/k\)</span> where
<span class="math inline">\(k\)</span> is an integer constant. In
general, it differs by at most a factor <span
class="math inline">\(\ln(4)\)</span> in the exponent of the time
bounds. As a consequence, LSH-based similarity search in Hamming space
can avoid the problem of false negatives at little or no cost in
efficiency.</p>
