---
layout: publication
title: Fast And Bayes-consistent Nearest Neighbors
authors: Efremenko Klim, Kontorovich Aryeh, Noivirt Moshe
conference: "Arxiv"
year: 2019
bibkey: efremenko2019fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1910.05270"}
tags: ['ARXIV', 'Independent', 'LSH']
---
<p>Research on nearest-neighbor methods tends to focus somewhat
dichotomously either on the statistical or the computational aspects –
either on, say, Bayes consistency and rates of convergence or on
techniques for speeding up the proximity search. This paper aims at
bridging these realms: to reap the advantages of fast evaluation time
while maintaining Bayes consistency, and further without sacrificing too
much in the risk decay rate. We combine the locality-sensitive hashing
(LSH) technique with a novel missing-mass argument to obtain a fast and
Bayes-consistent classifier. Our algorithm’s prediction runtime compares
favorably against state of the art approximate NN methods, while
maintaining Bayes-consistency and attaining rates comparable to minimax.
On samples of size <span class="math inline">\(n\)</span> in <span
class="math inline">\(\R^d\)</span>, our pre-processing phase has
runtime <span class="math inline">\(O(d n
\log n)\)</span>, while the evaluation phase has runtime <span
class="math inline">\(O(d\log n)\)</span> per query point.</p>
