---
layout: publication
title: Optimal Las Vegas Locality Sensitive Data Structures
authors: Ahle Thomas Dybdahl
conference: "Arxiv"
year: 2017
bibkey: ahle2017optimal
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1704.02054"}
tags: ['ARXIV', 'LSH', 'Unsupervised']
---
<p>We show that approximate similarity (near neighbour) search can be
solved in high dimensions with performance matching state of the art
(data independent) Locality Sensitive Hashing, but with a guarantee of
no false negatives. Specifically, we give two data structures for common
problems. For <span class="math inline">\(c\)</span>-approximate near
neighbour in Hamming space we get query time <span
class="math inline">\(dn^{1/c+o(1)}\)</span> and space <span
class="math inline">\(dn^{1+1/c+o(1)}\)</span> matching that of and
answering a long standing open question from~ and~ in the affirmative.
By means of a new deterministic reduction from <span
class="math inline">\(\ell_1\)</span> to Hamming we also solve <span
class="math inline">\(\ell_1\)</span> and <span
class="math inline">\(\ell_2\)</span> with query time <span
class="math inline">\(d^2n^{1/c+o(1)}\)</span> and space <span
class="math inline">\(d^2
n^{1+1/c+o(1)}\)</span>. For <span
class="math inline">\((s_1,s_2)\)</span>-approximate Jaccard similarity
we get query time <span class="math inline">\(dn^{\rho+o(1)}\)</span>
and space <span class="math inline">\(dn^{1+\rho+o(1)}\)</span>, <span
class="math inline">\(\rho=\log\frac{1+s_1}{2s_1}\big/\log\frac{1+s_2}{2s_2}\)</span>,
when sets have equal size, matching the performance of~. The algorithms
are based on space partitions, as with classic LSH, but we construct
these using a combination of brute force, tensoring, perfect hashing and
splitter functions `a la~. We also show a new dimensionality reduction
lemma with 1-sided error.</p>
