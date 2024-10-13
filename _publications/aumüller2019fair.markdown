---
layout: publication
title: Fair Near Neighbor Search Independent Range Sampling In High Dimensions
authors: Aumüller Martin, Pagh Rasmus, Silvestri Francesco
conference: "Arxiv"
year: 2019
bibkey: aumüller2019fair
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1906.01859"}
tags: ['ARXIV', 'Independent', 'LSH']
---
<p>Similarity search is a fundamental algorithmic primitive, widely used
in many computer science disciplines. There are several variants of the
similarity search problem, and one of the most relevant is the <span
class="math inline">\(r\)</span>-near neighbor (<span
class="math inline">\(r\)</span>-NN) problem: given a radius <span
class="math inline">\(r&gt;0\)</span> and a set of points <span
class="math inline">\(S\)</span>, construct a data structure that, for
any given query point <span class="math inline">\(q\)</span>, returns a
point <span class="math inline">\(p\)</span> within distance at most
<span class="math inline">\(r\)</span> from <span
class="math inline">\(q\)</span>. In this paper, we study the <span
class="math inline">\(r\)</span>-NN problem in the light of fairness. We
consider fairness in the sense of equal opportunity: all points that are
within distance <span class="math inline">\(r\)</span> from the query
should have the same probability to be returned. In the low-dimensional
case, this problem was first studied by Hu, Qiao, and Tao (PODS 2014).
Locality sensitive hashing (LSH), the theoretically strongest approach
to similarity search in high dimensions, does not provide such a
fairness guarantee. To address this, we propose efficient data
structures for <span class="math inline">\(r\)</span>-NN where all
points in <span class="math inline">\(S\)</span> that are near <span
class="math inline">\(q\)</span> have the same probability to be
selected and returned by the query. Specifically, we first propose a
black-box approach that, given any LSH scheme, constructs a data
structure for uniformly sampling points in the neighborhood of a query.
Then, we develop a data structure for fair similarity search under inner
product that requires nearly-linear space and exploits locality
sensitive filters. The paper concludes with an experimental evaluation
that highlights (un)fairness in a recommendation setting on real-world
datasets and discusses the inherent unfairness introduced by solving
other variants of the problem.</p>
