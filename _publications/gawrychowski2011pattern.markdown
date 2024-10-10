---
layout: publication
title: Pattern Matching In Lempel-ziv Compressed Strings Fast Simple And Deterministic
authors: Gawrychowski Pawel
conference: "Arxiv"
year: 2011
bibkey: gawrychowski2011pattern
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1104.4203"}
tags: ['ARXIV', 'Independent']
---
Countless variants of the Lempel-Ziv compression are widely used in many real-life applications. This paper is concerned with a natural modification of the classical pattern matching problem inspired by the popularity of such compression methods given an uncompressed pattern s1..m and a Lempel-Ziv representation of a string t1..N does s occur in t Farach and Thorup gave a randomized O(nlog^2(N/n)+m) time solution for this problem where n is the size of the compressed representation of t. We improve their result by developing a faster and fully deterministic O(nlog(N/n)+m) time algorithm with the same space complexity. Note that for highly compressible texts log(N/n) might be of order n so for such inputs the improvement is very significant. A (tiny) fragment of our method can be used to give an asymptotically optimal solution for the substring hashing problem considered by Farach and Muthukrishnan.
