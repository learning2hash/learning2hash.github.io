---
layout: publication
title: Simple Set Sketching
authors: "Jakob B\xE6k Tejs Houen, Rasmus Pagh, Stefan Walzer"
conference: Symposium on Simplicity in Algorithms (SOSA)
year: 2023
bibkey: houen2022simple
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.03683'}]
tags: ["Hashing Methods"]
short_authors: "Jakob B\xE6k Tejs Houen, Rasmus Pagh, Stefan Walzer"
---
Imagine handling collisions in a hash table by storing, in each cell, the
bit-wise exclusive-or of the set of keys hashing there. This appears to be a
terrible idea: For \\(\alpha n\\) keys and \\(n\\) buckets, where \\(\alpha\\) is constant,
we expect that a constant fraction of the keys will be unrecoverable due to
collisions.
  We show that if this collision resolution strategy is repeated three times
independently the situation reverses: If \\(\alpha\\) is below a threshold of
\\(\approx 0.81\\) then we can recover the set of all inserted keys in linear time
with high probability.
  Even though the description of our data structure is simple, its analysis is
nontrivial. Our approach can be seen as a variant of the Invertible Bloom
Filter (IBF) of Eppstein and Goodrich. While IBFs involve an explicit checksum
per bucket to decide whether the bucket stores a single key, we exploit the
idea of quotienting, namely that some bits of the key are implicit in the
location where it is stored. We let those serve as an implicit checksum. These
bits are not quite enough to ensure that no errors occur and the main technical
challenge is to show that decoding can recover from these errors.