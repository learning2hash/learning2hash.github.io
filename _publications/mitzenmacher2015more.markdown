---
layout: publication
title: More Analysis Of Double Hashing For Balanced Allocations
authors: Mitzenmacher Michael
conference: "Arxiv"
year: 2015
bibkey: mitzenmacher2015more
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1503.00658"}
tags: ['ARXIV', 'Independent']
---
<p>With double hashing, for a key <span
class="math inline">\(x\)</span>, one generates two hash values <span
class="math inline">\(f(x)\)</span> and <span
class="math inline">\(g(x)\)</span>, and then uses combinations <span
class="math inline">\((f(x) +i g(x)) \bmod n\)</span> for <span
class="math inline">\(i=0,1,2,...\)</span> to generate multiple hash
values in the range <span class="math inline">\([0,n-1]\)</span> from
the initial two. For balanced allocations, keys are hashed into a hash
table where each bucket can hold multiple keys, and each key is placed
in the least loaded of <span class="math inline">\(d\)</span> choices.
It has been shown previously that asymptotically the performance of
double hashing and fully random hashing is the same in the balanced
allocation paradigm using fluid limit methods. Here we extend a coupling
argument used by Lueker and Molodowitch to show that double hashing and
ideal uniform hashing are asymptotically equivalent in the setting of
open address hash tables to the balanced allocation setting, providing
further insight into this phenomenon. We also discuss the potential for
and bottlenecks limiting the use this approach for other multiple choice
hashing schemes.</p>
