---
layout: publication
title: Probability Distributions For Elliptic Curves In The CGL Hash Function
authors: Dhruv Bhatia, Kara Fagerstrom, Maximillian Watson
conference: Arxiv
year: 2021
bibkey: bhatia2021probability
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.06457'}]
tags: ["Hashing Methods"]
short_authors: Dhruv Bhatia, Kara Fagerstrom, Maximillian Watson
---
Hash functions map data of arbitrary length to data of predetermined length.
Good hash functions are hard to predict, making them useful in cryptography. We
are interested in the elliptic curve CGL hash function, which maps a bitstring
to an elliptic curve by traversing an input-determined path through an isogeny
graph. The nodes of an isogeny graph are elliptic curves, and the edges are
special maps betwixt elliptic curves called isogenies. Knowing which hash
values are most likely informs us of potential security weaknesses in the hash
function. We use stochastic matrices to compute the expected probability
distributions of the hash values. We generalize our experimental data into a
theorem that completely describes all possible probability distributions of the
CGL hash function. We use this theorem to evaluate the collision resistance of
the CGL hash function and compare this to the collision resistance of an
"ideal" hash function.