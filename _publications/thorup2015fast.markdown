---
layout: publication
title: Fast and Powerful Hashing using Tabulation
authors: Thorup Mikkel
conference: Arxiv
year: 2015
bibkey: thorup2015fast
additional_links:
   - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1505.01523"}
tags: ['Arxiv', 'Survey Paper']
---
Randomized algorithms are often enjoyed for their simplicity, but the hash functions employed to yield the desired probabilistic guarantees are often too complicated to be practical. Here we survey recent results on how simple hashing schemes based on tabulation provide unexpectedly strong guarantees. Simple tabulation hashing dates back to Zobrist [1970]. Keys are viewed as consisting of $c$ characters and we have precomputed character tables $h_1,...,h_c$ mapping characters to random hash values. A key $x=(x_1,...,x_c)$ is hashed to $h_1[x_1] \oplus h_2[x_2].....\oplus h_c[x_c]$. This schemes is very fast with character tables in cache. While simple tabulation is not even 4-independent, it does provide many of the guarantees that are normally obtained via higher independence, e.g., linear probing and Cuckoo hashing. Next we consider twisted tabulation where one input character is "twisted" in a simple way. The resulting hash function has powerful distributional properties: Chernoff-Hoeffding type tail bounds and a very small bias for min-wise hashing. This also yields an extremely fast pseudo-random number generator that is provably good for many classic randomized algorithms and data-structures. Finally, we consider double tabulation where we compose two simple tabulation functions, applying one to the output of the other, and show that this yields very high independence in the classic framework of Carter and Wegman [1977]. In fact, w.h.p., for a given set of size proportional to that of the space consumed, double tabulation gives fully-random hashing. We also mention some more elaborate tabulation schemes getting near-optimal independence for given time and space. While these tabulation schemes are all easy to implement and use, their analysis is not.
