---
layout: publication
title: Linear Hashing Is Awesome
authors: "Mathias B\xE6k Tejs Knudsen"
conference: 2016 IEEE 57th Annual Symposium on Foundations of Computer Science (FOCS)
year: 2016
bibkey: knudsen2016linear
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.02783'}]
tags: ["Hashing Methods"]
short_authors: "Mathias B\xE6k Tejs Knudsen"
---
We consider the hash function \(h(x) = ((ax+b) \bmod p) \bmod n\) where \(a,b\)
are chosen uniformly at random from \(\\{0,1,\ldots,p-1\\}\). We prove that when we
use \(h(x)\) in hashing with chaining to insert \(n\) elements into a table of size
\(n\) the expected length of the longest chain is
\(\tilde\{O\}\!\left(n^\{1/3\}\right)\). The proof also generalises to give the same
bound when we use the multiply-shift hash function by Dietzfelbinger et al.
[Journal of Algorithms 1997].