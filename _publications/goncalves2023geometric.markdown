---
layout: publication
title: Geometric Covering Using Random Fields
authors: Goncalves Felipe, Keren Daniel, Shahar Amit, Yehuda Gal
conference: "Arxiv"
year: 2023
bibkey: goncalves2023geometric
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2311.14082"}
tags: ['ARXIV', 'Independent', 'LSH']
---
<p>A set of vectors <span class="math inline">\(S \subseteq
\mathbb{R}^d\)</span> is <span
class="math inline">\((k_1,\varepsilon)\)</span>-clusterable if there
are <span class="math inline">\(k_1\)</span> balls of radius <span
class="math inline">\(\varepsilon\)</span> that cover <span
class="math inline">\(S\)</span>. A set of vectors <span
class="math inline">\(S \subseteq \mathbb{R}^d\)</span> is <span
class="math inline">\((k_2,\delta)\)</span>-far from being clusterable
if there are at least <span class="math inline">\(k_2\)</span> vectors
in <span class="math inline">\(S\)</span>, with all pairwise distances
at least <span class="math inline">\(\delta\)</span>. We propose a
probabilistic algorithm to distinguish between these two cases. Our
algorithm reaches a decision by only looking at the extreme values of a
scalar valued hash function, defined by a random field, on <span
class="math inline">\(S\)</span>; hence, it is especially suitable in
distributed and online settings. An important feature of our method is
that the algorithm is oblivious to the number of vectors: in the online
setting, for example, the algorithm stores only a constant number of
scalars, which is independent of the stream length. We introduce random
field hash functions, which are a key ingredient in our paradigm. Random
field hash functions generalize locality-sensitive hashing (LSH). In
addition to the LSH requirement that
<code>nearby vectors are hashed to similar values", our hash function also guarantees that the</code>hash
values are (nearly) independent random variables for distant vectors”.
We formulate necessary conditions for the kernels which define the
random fields applied to our problem, as well as a measure of kernel
optimality, for which we provide a bound. Then, we propose a method to
construct kernels which approximate the optimal one.</p>
