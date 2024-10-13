---
layout: publication
title: Data-dependent LSH For The Earth Movers Distance
authors: Jayaram Rajesh, Waingarten Erik, Zhang Tian
conference: "Arxiv"
year: 2024
bibkey: jayaram2024data
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2403.05041"}
tags: ['ARXIV', 'Independent', 'LSH']
---
<p>We give new data-dependent locality sensitive hashing schemes (LSH)
for the Earth Mover’s Distance (<span
class="math inline">\(\mathsf{EMD}\)</span>), and as a result, improve
the best approximation for nearest neighbor search under <span
class="math inline">\(\mathsf{EMD}\)</span> by a quadratic factor. Here,
the metric <span
class="math inline">\(\mathsf{EMD}_s(\mathbb{R}^d,\ell_p)\)</span>
consists of sets of <span class="math inline">\(s\)</span> vectors in
<span class="math inline">\(\mathbb{R}^d\)</span>, and for any two sets
<span class="math inline">\(x,y\)</span> of <span
class="math inline">\(s\)</span> vectors the distance <span
class="math inline">\(\mathsf{EMD}(x,y)\)</span> is the minimum cost of
a perfect matching between <span class="math inline">\(x,y\)</span>,
where the cost of matching two vectors is their <span
class="math inline">\(\ell_p\)</span> distance. Previously, Andoni,
Indyk, and Krauthgamer gave a (data-independent) locality-sensitive
hashing scheme for <span
class="math inline">\(\mathsf{EMD}_s(\mathbb{R}^d,\ell_p)\)</span> when
<span class="math inline">\(p \in [1,2]\)</span> with approximation
<span class="math inline">\(O(\log^2 s)\)</span>. By being
data-dependent, we improve the approximation to <span
class="math inline">\(\tilde{O}(\log s)\)</span>. Our main technical
contribution is to show that for any distribution <span
class="math inline">\(\mu\)</span> supported on the metric <span
class="math inline">\(\mathsf{EMD}_s(\mathbb{R}^d, \ell_p)\)</span>,
there exists a data-dependent LSH for dense regions of <span
class="math inline">\(\mu\)</span> which achieves approximation <span
class="math inline">\(\tilde{O}(\log s)\)</span>, and that the
data-independent LSH actually achieves a <span
class="math inline">\(\tilde{O}(\log s)\)</span>-approximation outside
of those dense regions. Finally, we show how to “glue” together these
two hashing schemes without any additional loss in the approximation.
Beyond nearest neighbor search, our data-dependent LSH also gives
optimal (distributional) sketches for the Earth Mover’s Distance. By
known sketching lower bounds, this implies that our LSH is optimal (up
to <span class="math inline">\(\mathrm{poly}(\log
\log s)\)</span> factors) among those that collide close points with
constant probability.</p>
