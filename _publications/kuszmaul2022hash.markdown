---
layout: publication
title: A Hash Table Without Hash Functions And How To Get The Most Out Of Your Random Bits
authors: Kuszmaul William
conference: "Arxiv"
year: 2022
bibkey: kuszmaul2022hash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2209.06038"}
tags: ['ARXIV', 'Independent']
---
<p>This paper considers the basic question of how strong of a
probabilistic guarantee can a hash table, storing <span
class="math inline">\(n\)</span> <span class="math inline">\((1 +
\Theta(1)) \log n\)</span>-bit key/value pairs, offer? Past work on this
question has been bottlenecked by limitations of the known families of
hash functions: The only hash tables to achieve failure probabilities
less than <span class="math inline">\(1 / 2^{\polylog n}\)</span>
require access to fully-random hash functions – if the same hash tables
are implemented using the known explicit families of hash functions,
their failure probabilities become <span class="math inline">\(1 /
\poly(n)\)</span>. To get around these obstacles, we show how to
construct a randomized data structure that has the same guarantees as a
hash table, but that . Building on this, we are able to construct a hash
table using <span class="math inline">\(O(n)\)</span> random bits that
achieves failure probability <span class="math inline">\(1 /
n^{n^{1 - \epsilon}}\)</span> for an arbitrary positive constant <span
class="math inline">\(\epsilon\)</span>. In fact, we show that this
guarantee can even be achieved by a , that is, by a dictionary that uses
space within a <span class="math inline">\(1 + o(1)\)</span> factor of
the information-theoretic optimum. Finally we also construct a succinct
hash table whose probabilistic guarantees fall on a different extreme,
offering a failure probability of <span class="math inline">\(1 /
\poly(n)\)</span> while using only <span
class="math inline">\(\tilde{O}(\log n)\)</span> random bits. This
latter result matches (up to low-order terms) a guarantee previously
achieved by Dietzfelbinger et al., but with increased space efficiency
and with several surprising technical components.</p>
