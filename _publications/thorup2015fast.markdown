---
layout: publication
title: Fast And Powerful Hashing Using Tabulation
authors: Thorup Mikkel
conference: "Arxiv"
year: 2015
bibkey: thorup2015fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1505.01523"}
tags: ['ARXIV', 'Independent', 'Survey Paper']
---
Randomized algorithms are often enjoyed for their simplicity but the hash functions employed to yield the desired probabilistic guarantees are often too complicated to be practical. Here we survey recent results on how simple hashing schemes based on tabulation provide unexpectedly strong guarantees. Simple tabulation hashing dates back to Zobrist 1970. Keys are viewed as consisting of c characters and we have precomputed character tables h95;1...h95;c mapping characters to random hash values. A key x=(x95;1...x95;c) is hashed to h95;1x95;1 oplus h95;2x95;2.....oplus h95;cx95;c. This schemes is very fast with character tables in cache. While simple tabulation is not even 445;independent it does provide many of the guarantees that are normally obtained via higher independence e.g. linear probing and Cuckoo hashing. Next we consider twisted tabulation where one input character is twisted in a simple way. The resulting hash function has powerful distributional properties Chernoff45;Hoeffding type tail bounds and a very small bias for min45;wise hashing. This also yields an extremely fast pseudo45;random number generator that is provably good for many classic randomized algorithms and data45;structures. Finally we consider double tabulation where we compose two simple tabulation functions applying one to the output of the other and show that this yields very high independence in the classic framework of Carter and Wegman 1977. In fact w.h.p. for a given set of size proportional to that of the space consumed double tabulation gives fully45;random hashing. We also mention some more elaborate tabulation schemes getting near45;optimal independence for given time and space. While these tabulation schemes are all easy to implement and use their analysis is not.
