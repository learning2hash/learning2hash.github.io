---
layout: publication
title: Locality-preserving Minimal Perfect Hashing Of K-mers
authors: Pibiri Giulio Ermanno, Shibuya Yoshihiro, Limasset Antoine
conference: "Arxiv"
year: 2022
bibkey: pibiri2022locality
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2210.13097"}
tags: ['ARXIV', 'Independent']
---
<p>Minimal perfect hashing is the problem of mapping a static set of
<span class="math inline">\(n\)</span> distinct keys into the address
space <span class="math inline">\(\{1,\ldots,n\}\)</span> bijectively.
It is well-known that <span class="math inline">\(n\log_2(e)\)</span>
bits are necessary to specify a minimal perfect hash function (MPHF)
<span class="math inline">\(f\)</span>, when no additional knowledge of
the input keys is to be used. However, it is often the case in practice
that the input keys have intrinsic relationships that we can exploit to
lower the bit complexity of <span class="math inline">\(f\)</span>. For
example, consider a string and the set of all its distinct <span
class="math inline">\(k\)</span>-mers as input keys: since two
consecutive <span class="math inline">\(k\)</span>-mers share an overlap
of <span class="math inline">\(k-1\)</span> symbols, it seems possible
to beat the classic <span class="math inline">\(\log_2(e)\)</span>
bits/key barrier in this case. Moreover, we would like <span
class="math inline">\(f\)</span> to map consecutive <span
class="math inline">\(k\)</span>-mers to consecutive addresses, as to
also preserve as much as possible their relationship in the codomain.
This is a useful feature in practice as it guarantees a certain degree
of locality of reference for <span class="math inline">\(f\)</span>,
resulting in a better evaluation time when querying consecutive <span
class="math inline">\(k\)</span>-mers. Motivated by these premises, we
initiate the study of a new type of locality-preserving MPHF designed
for <span class="math inline">\(k\)</span>-mers extracted consecutively
from a collection of strings. We design a construction whose space usage
decreases for growing <span class="math inline">\(k\)</span> and discuss
experiments with a practical implementation of the method: in practice,
the functions built with our method can be several times smaller and
even faster to query than the most efficient MPHFs in the
literature.</p>
