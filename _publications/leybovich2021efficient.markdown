---
layout: publication
title: Efficient Approximate Search For Sets Of Vectors
authors: Leybovich Michael, Shmueli Oded
conference: "Arxiv"
year: 2021
bibkey: leybovich2021efficient
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2107.06817"}
tags: ['ARXIV', 'Graph', 'Independent', 'LSH', 'Quantisation']
---
<p>We consider a similarity measure between two sets <span
class="math inline">\(A\)</span> and <span
class="math inline">\(B\)</span> of vectors, that balances the average
and maximum cosine distance between pairs of vectors, one from set <span
class="math inline">\(A\)</span> and one from set <span
class="math inline">\(B\)</span>. As a motivation for this measure, we
present lineage tracking in a database. To practically realize this
measure, we need an approximate search algorithm that given a set of
vectors <span class="math inline">\(A\)</span> and sets of vectors <span
class="math inline">\(B_1,...,B_n\)</span>, the algorithm quickly
locates the set <span class="math inline">\(B_i\)</span> that maximizes
the similarity measure. For the case where all sets are singleton sets,
essentially each is a single vector, there are known efficient
approximate search algorithms, e.g., approximated versions of tree
search algorithms, locality-sensitive hashing (LSH), vector quantization
(VQ) and proximity graph algorithms. In this work, we present
approximate search algorithms for the general case. The underlying idea
in these algorithms is encoding a set of vectors via a “long” single
vector. The proposed approximate approach achieves significant
performance gains over an optimized, exact search on vector sets.</p>
