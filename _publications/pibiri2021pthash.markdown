---
layout: publication
title: Pthash Revisiting FCH Minimal Perfect Hashing
authors: Pibiri Giulio Ermanno, Trani Roberto
conference: "SIGIR"
year: 2021
bibkey: pibiri2021pthash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2104.10402"}
tags: ['Independent', 'SIGIR']
---
<p>Given a set <span class="math inline">\(S\)</span> of <span
class="math inline">\(n\)</span> distinct keys, a function <span
class="math inline">\(f\)</span> that bijectively maps the keys of <span
class="math inline">\(S\)</span> into the range <span
class="math inline">\(\{0,\ldots,n-1\}\)</span> is called a minimal
perfect hash function for <span class="math inline">\(S\)</span>.
Algorithms that find such functions when <span
class="math inline">\(n\)</span> is large and retain constant evaluation
time are of practical interest; for instance, search engines and
databases typically use minimal perfect hash functions to quickly assign
identifiers to static sets of variable-length keys such as strings. The
challenge is to design an algorithm which is efficient in three
different aspects: time to find <span class="math inline">\(f\)</span>
(construction time), time to evaluate <span
class="math inline">\(f\)</span> on a key of <span
class="math inline">\(S\)</span> (lookup time), and space of
representation for <span class="math inline">\(f\)</span>. Several
algorithms have been proposed to trade-off between these aspects. In
1992, Fox, Chen, and Heath (FCH) presented an algorithm at SIGIR
providing very fast lookup evaluation. However, the approach received
little attention because of its large construction time and higher space
consumption compared to other subsequent techniques. Almost thirty years
later we revisit their framework and present an improved algorithm that
scales well to large sets and reduces space consumption altogether,
without compromising the lookup time. We conduct an extensive
experimental assessment and show that the algorithm finds functions that
are competitive in space with state-of-the art techniques and provide
<span class="math inline">\(2-4\times\)</span> better lookup time.</p>
