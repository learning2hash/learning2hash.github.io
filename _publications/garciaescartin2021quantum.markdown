---
layout: publication
title: Quantum Collision Finding For Homomorphic Hash Functions
authors: "Juan Carlos Garcia-Escartin, Vicent Gimeno, Julio Jos\xE9 Moyano-Fern\xE1\
  ndez"
conference: Arxiv
year: 2021
bibkey: garciaescartin2021quantum
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.00100'}]
tags: ["Hashing Methods"]
short_authors: "Juan Carlos Garcia-Escartin, Vicent Gimeno, Julio Jos\xE9 Moyano-Fern\xE1\
  ndez"
---
Hash functions are a basic cryptographic primitive. Certain hash functions
try to prove security against collision and preimage attacks by reductions to
known hard problems. These hash functions usually have some additional
properties that allow for that reduction. Hash functions which are additive or
multiplicative are vulnerable to a quantum attack using the hidden subgroup
problem algorithm for quantum computers. Using a quantum oracle to the hash, we
can reconstruct the kernel of the hash function, which is enough to find
collisions and second preimages. When the hash functions are additive with
respect to the group operation in an Abelian group, there is always an
efficient implementation of this attack. We present concrete attack examples to
provable hash functions, including a preimage attack to \(\oplus\)-linear hash
functions and for certain multiplicative homomorphic hash schemes.