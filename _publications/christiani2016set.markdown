---
layout: publication
title: Set Similarity Search Beyond Minhash
authors: Christiani Tobias, Pagh Rasmus
conference: "Arxiv"
year: 2016
bibkey: christiani2016set
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1612.07710"}
tags: ['ARXIV', 'Independent', 'LSH']
---
<p>We consider the problem of approximate set similarity search under
Braun-Blanquet similarity <span class="math inline">\(B(\mathbf{x},
\mathbf{y}) = |\mathbf{x} \cap
\mathbf{y}| / \max(|\mathbf{x}|, |\mathbf{y}|)\)</span>. The <span
class="math inline">\((b_2, b_2)\)</span>-approximate Braun-Blanquet
similarity search problem is to preprocess a collection of sets <span
class="math inline">\(P\)</span> such that, given a query set <span
class="math inline">\(\mathbf{q}\)</span>, if there exists <span
class="math inline">\(\mathbf{x} \in
P\)</span> with <span class="math inline">\(B(\mathbf{q}, \mathbf{x})
\geq b_1\)</span>, then we can efficiently return <span
class="math inline">\(\mathbf{x}&#39; \in P\)</span> with <span
class="math inline">\(B(\mathbf{q}, \mathbf{x}&#39;) &gt; b_2\)</span>.
We present a simple data structure that solves this problem with space
usage <span class="math inline">\(O(n^{1+\rho}\log n + \sum_{\mathbf{x}
\in P}|\mathbf{x}|)\)</span> and query time <span
class="math inline">\(O(|\mathbf{q}|n^{\rho} \log n)\)</span> where
<span class="math inline">\(n = |P|\)</span> and <span
class="math inline">\(\rho =
\log(1/b_1)/\log(1/b_2)\)</span>. Making use of existing lower bounds
for locality-sensitive hashing by O’Donnell et al. (TOCT 2014) we show
that this value of <span class="math inline">\(\rho\)</span> is tight
across the parameter space, i.e., for every choice of constants <span
class="math inline">\(0 &lt; b_2 &lt; b_1 &lt; 1\)</span>. In the case
where all sets have the same size our solution strictly improves upon
the value of <span class="math inline">\(\rho\)</span> that can be
obtained through the use of state-of-the-art data-independent techniques
in the Indyk-Motwani locality-sensitive hashing framework (STOC 1998)
such as Broder’s MinHash (CCS 1997) for Jaccard similarity and Andoni et
al.’s cross-polytope LSH (NIPS 2015) for cosine similarity.
Surprisingly, even though our solution is data-independent, for a large
part of the parameter space we outperform the currently best
data-dependent method by Andoni and Razenshteyn (STOC 2015).</p>
