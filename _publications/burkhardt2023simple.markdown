---
layout: publication
title: Simple And Efficient Four-cycle Counting On Sparse Graphs
authors: Burkhardt Paul, Harris David G.
conference: "Arxiv"
year: 2023
bibkey: burkhardt2023simple
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2303.06090"}
tags: ['ARXIV', 'Graph']
---
<p>We consider the problem of counting 4-cycles (<span
class="math inline">\(C_4\)</span>) in an undirected graph <span
class="math inline">\(G\)</span> of <span
class="math inline">\(n\)</span> vertices and <span
class="math inline">\(m\)</span> edges (in bipartite graphs, 4-cycles
are also often referred to as <span
class="math inline">\(\textit{butterflies}\)</span>). Most recently,
Wang et al. (2019, 2022) developed algorithms for this problem based on
hash tables and sorting the graph by degree. Their algorithm takes <span
class="math inline">\(O(m\bar\delta)\)</span> expected time and <span
class="math inline">\(O(m)\)</span> space, where <span
class="math inline">\(\bar \delta \leq O(\sqrt{m})\)</span> is the <span
class="math inline">\(\textit{average
degeneracy}\)</span> parameter introduced by Burkhardt, Faber &amp;
Harris (2020). We develop a streamlined version of this algorithm
requiring <span class="math inline">\(O(m\bar\delta)\)</span> time and
precisely <span class="math inline">\(n\)</span> words of space. It has
several practical improvements and optimizations; for example, it is
fully deterministic, does not require any auxiliary storage or sorting
of the input graph, and uses only addition and array access in its inner
loops. Our algorithm is very simple and easily adapted to count 4-cycles
incident to each vertex and edge. Empirical tests demonstrate that our
array-based approach is <span class="math inline">\(4\times\)</span> –
<span class="math inline">\(7\times\)</span> faster on average compared
to popular hash table implementations.</p>
