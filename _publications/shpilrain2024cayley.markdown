---
layout: publication
title: "Cayley hashing with cookies"
authors: Shpilrain Vladimir, Sosnovski Bianca
conference: Arxiv
year: 2024
bibkey: shpilrain2024cayley
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/2402.04943"}
tags: ['ARXIV', 'TIP']
---
Cayley hash functions are based on a simple idea of using a pair of semigroup elements, A and B, to hash the 0 and 1 bit, respectively, and then to hash an arbitrary bit string in the natural way, by using multiplication of elements in the semigroup. The main advantage of Cayley hash functions compared to, say, hash functions in the SHA family is that when an already hashed document is amended, one does not have to hash the whole amended document all over again, but rather hash just the amended part and then multiply the result by the hash of the original document. Some authors argued that this may be a security hazard, specifically that this property may facilitate finding a second preimage by splitting a long bit string into shorter pieces. In this paper, we offer a way to get rid of this alleged disadvantage and keep the advantages at the same time. We call this method ``Cayley hashing with cookies" using terminology borrowed from the theory of random walks in a random environment. For the platform semigroup, we use 2x2 matrices over F_p.