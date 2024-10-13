---
layout: publication
title: On The Maximal Independent Sets Of k-mers With The Edit Distance
authors: Ma Leran, Chen Ke, Shao Mingfu
conference: "Arxiv"
year: 2023
bibkey: ma2023maximal
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2303.10926"}
  - {name: "Code", url: "https://github.com/Shao-Group/kmerspace"}
tags: ['ARXIV', 'Graph', 'Has Code', 'Independent']
---
<p>In computational biology, <span class="math inline">\(k\)</span>-mers
and edit distance are fundamental concepts. However, little is known
about the metric space of all <span
class="math inline">\(k\)</span>-mers equipped with the edit distance.
In this work, we explore the structure of the <span
class="math inline">\(k\)</span>-mer space by studying its maximal
independent sets (MISs). An MIS is a sparse sketch of all <span
class="math inline">\(k\)</span>-mers with nice theoretical properties,
and therefore admits critical applications in clustering, indexing,
hashing, and sketching large-scale sequencing data, particularly those
with high error-rates. Finding an MIS is a challenging problem, as the
size of a <span class="math inline">\(k\)</span>-mer space grows
geometrically with respect to <span class="math inline">\(k\)</span>. We
propose three algorithms for this problem. The first and the most
intuitive one uses a greedy strategy. The second method implements two
techniques to avoid redundant comparisons by taking advantage of the
locality-property of the <span class="math inline">\(k\)</span>-mer
space and the estimated bounds on the edit distance. The last algorithm
avoids expensive calculations of the edit distance by translating the
edit distance into the shortest path in a specifically designed graph.
These algorithms are implemented and the calculated MISs of <span
class="math inline">\(k\)</span>-mer spaces and their statistical
properties are reported and analyzed for <span
class="math inline">\(k\)</span> up to 15. Source code is freely
available at https://github.com/Shao-Group/kmerspace .</p>
