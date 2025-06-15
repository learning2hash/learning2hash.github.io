---
layout: publication
title: Halftimehash Modern Hashing Without 64-bit Multipliers Or Finite Fields
authors: Apple Jim
conference: "Arxiv"
year: 2021
citations: 0
bibkey: apple2021halftimehash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2104.08865"}
tags: ['ARXIV', 'Independent']
---
HalftimeHash is a new algorithm for hashing long strings. The goals are few
collisions (different inputs that produce identical output hash values) and
high performance.
  Compared to the fastest universal hash functions on long strings (clhash and
UMASH) HalftimeHash decreases collision probability while also increasing
performance by over 50%, exceeding 16 bytes per cycle. In addition,
HalftimeHash does not use any widening 64-bit multiplications or any finite
field arithmetic that could limit its portability.
