---
layout: publication
title: A Fast Generic Sequence Matching Algorithm
authors: Musser David R., Nishanov Gor V.
conference: "Arxiv"
year: 2008
bibkey: musser2008fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/0810.0264"}
tags: ['ARXIV', 'Independent']
---
A string matching -- and more generally sequence matching -- algorithm is presented that has a linear worst-case computing time bound a low worst-case bound on the number of comparisons (2n) and sublinear average-case behavior that is better than that of the fastest versions of the Boyer-Moore algorithm. The algorithm retains its efficiency advantages in a wide variety of sequence matching problems of practical interest including traditional string matching; large-alphabet problems (as in Unicode strings); and small-alphabet long-pattern problems (as in DNA searches). Since it is expressed as a generic algorithm for searching in sequences over an arbitrary type T it is well suited for use in generic software libraries such as the C++ Standard Template Library. The algorithm was obtained by adding to the Knuth-Morris-Pratt algorithm one of the pattern-shifting techniques from the Boyer-Moore algorithm with provision for use of hashing in this technique. In situations in which a hash function or random access to the sequences is not available the algorithm falls back to an optimized version of the Knuth-Morris-Pratt algorithm.
