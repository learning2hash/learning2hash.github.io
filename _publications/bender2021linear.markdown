---
layout: publication
title: Linear Probing Revisited Tombstones Mark The Death Of Primary Clustering
authors: Bender Michael A., Kuszmaul Bradley C., Kuszmaul William
conference: "Arxiv"
year: 2021
bibkey: bender2021linear
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2107.01250"}
tags: ['ARXIV', 'Unsupervised']
---
<p>First introduced in 1954, linear probing is one of the oldest data
structures in computer science, and due to its unrivaled data locality,
it continues to be one of the fastest hash tables in practice. It is
widely believed and taught, however, that linear probing should never be
used at high load factors; this is because primary-clustering effects
cause insertions at load factor <span class="math inline">\(1 - 1
/x\)</span> to take expected time <span
class="math inline">\(\Theta(x^2)\)</span> (rather than the ideal <span
class="math inline">\(\Theta(x)\)</span>). The dangers of primary
clustering, first discovered by Knuth in 1963, have been taught to
generations of computer scientists, and have influenced the design of
some of many widely used hash tables. We show that primary clustering is
not a foregone conclusion. We demonstrate that small design decisions in
how deletions are implemented have dramatic effects on the asymptotic
performance of insertions, so that, even if a hash table operates
continuously at a load factor <span class="math inline">\(1 -
\Theta(1/x)\)</span>, the expected amortized cost per operation is <span
class="math inline">\(\tilde{O}(x)\)</span>. This is because tombstones
created by deletions actually cause an anti-clustering effect that
combats primary clustering. We also present a new variant of linear
probing (which we call graveyard hashing) that completely eliminates
primary clustering on sequence of operations: if, when an operation is
performed, the current load factor is <span class="math inline">\(1 -
1/x\)</span> for some <span class="math inline">\(x\)</span>, then the
expected cost of the operation is <span
class="math inline">\(O(x)\)</span>. One corollary is that, in the
external-memory model with a data blocks of size <span
class="math inline">\(B\)</span>, graveyard hashing offers the following
remarkable guarantee: at any load factor <span class="math inline">\(1 -
1/x\)</span> satisfying <span class="math inline">\(x = o(B)\)</span>,
graveyard hashing achieves <span class="math inline">\(1 + o(1)\)</span>
expected block transfers per operation. Past external-memory hash tables
have only been able to offer a <span class="math inline">\(1 +
o(1)\)</span> guarantee when the block size <span
class="math inline">\(B\)</span> is at least <span
class="math inline">\(\Omega(x^2)\)</span>.</p>
