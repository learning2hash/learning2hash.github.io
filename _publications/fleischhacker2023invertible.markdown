---
layout: publication
title: Invertible Bloom Lookup Tables With Less Memory And Randomness
authors: Fleischhacker Nils, Larsen Kasper Green, Obremski Maciej, Simkin Mark
conference: "Arxiv"
year: 2023
bibkey: fleischhacker2023invertible
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2306.07583"}
tags: ['ARXIV', 'Graph', 'Independent']
---
<p>In this work we study Invertible Bloom Lookup Tables (IBLTs) with
small failure probabilities. IBLTs are highly versatile data structures
that have found applications in set reconciliation protocols,
error-correcting codes, and even the design of advanced cryptographic
primitives. For storing <span class="math inline">\(n\)</span> elements
and ensuring correctness with probability at least <span
class="math inline">\(1 - \delta\)</span>, existing IBLT constructions
require <span
class="math inline">\(\Omega(n(\frac{\log(1/\delta)}{\log(n)}+1))\)</span>
space and they crucially rely on fully random hash functions. We present
new constructions of IBLTs that are simultaneously more space efficient
and require less randomness. For storing <span
class="math inline">\(n\)</span> elements with a failure probability of
at most <span class="math inline">\(\delta\)</span>, our data structure
only requires <span class="math inline">\(\mathcal{O}(n +
\log(1/\delta)\log\log(1/\delta))\)</span> space and <span
class="math inline">\(\mathcal{O}(\log(\log(n)/\delta))\)</span>-wise
independent hash functions. As a key technical ingredient we show that
hashing <span class="math inline">\(n\)</span> keys with any <span
class="math inline">\(k\)</span>-wise independent hash function <span
class="math inline">\(h:U \to [Cn]\)</span> for some sufficiently large
constant <span class="math inline">\(C\)</span> guarantees with
probability <span class="math inline">\(1 - 2^{-\Omega(k)}\)</span> that
at least <span class="math inline">\(n/2\)</span> keys will have a
unique hash value. Proving this is highly non-trivial as <span
class="math inline">\(k\)</span> approaches <span
class="math inline">\(n\)</span>. We believe that the techniques used to
prove this statement may be of independent interest.</p>
