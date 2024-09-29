---
layout: publication
title: Fast Locality45;sensitive Hashing Frameworks For Approximate Near Neighbor Search
authors: Christiani Tobias
conference: "Arxiv"
year: 2017
bibkey: christiani2017fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1708.07586"}
tags: ['ARXIV', 'FOCS', 'Independent', 'LSH']
---
The Indyk45;Motwani Locality45;Sensitive Hashing (LSH) framework (STOC 1998) is a general technique for constructing a data structure to answer approximate near neighbor queries by using a distribution mathcal123;H125; over locality45;sensitive hash functions that partition space. For a collection of n points after preprocessing the query time is dominated by O(n^123;ρ125; log n) evaluations of hash functions from mathcal123;H125; and O(n^123;ρ125;) hash table lookups and distance computations where ρ in (01) is determined by the locality45;sensitivity properties of mathcal123;H125;. It follows from a recent result by Dahlgaard et al. (FOCS 2017) that the number of locality45;sensitive hash functions can be reduced to O(log^2 n) leaving the query time to be dominated by O(n^123;ρ125;) distance computations and O(n^123;ρ125; log n) additional word45;RAM operations. We state this result as a general framework and provide a simpler analysis showing that the number of lookups and distance computations closely match the Indyk45;Motwani framework making it a viable replacement in practice. Using ideas from another locality45;sensitive hashing framework by Andoni and Indyk (SODA 2006) we are able to reduce the number of additional word45;RAM operations to O(n^ρ).
