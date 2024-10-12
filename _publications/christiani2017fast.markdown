---
layout: publication
title: Fast Locality-sensitive Hashing Frameworks For Approximate Near Neighbor Search
authors: Christiani Tobias
conference: "Arxiv"
year: 2017
bibkey: christiani2017fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1708.07586"}
tags: ['ARXIV', 'FOCS', 'Independent', 'LSH']
---
The Indyk-Motwani Locality-Sensitive Hashing (LSH) framework (STOC 1998) is a general technique for constructing a data structure to answer approximate near neighbor queries by using a distribution \{&#37; raw &#37;\}\\(\mathcal\{H\}\\)\{&#37; endraw &#37;\} over locality-sensitive hash functions that partition space. For a collection of \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\} points, after preprocessing, the query time is dominated by \{&#37; raw &#37;\}\\(O(n^\{\rho\} \log n)\\)\{&#37; endraw &#37;\} evaluations of hash functions from \{&#37; raw &#37;\}\\(\mathcal\{H\}\\)\{&#37; endraw &#37;\} and \{&#37; raw &#37;\}\\(O(n^\{\rho\})\\)\{&#37; endraw &#37;\} hash table lookups and distance computations where \{&#37; raw &#37;\}\\(\rho \in (0,1)\\)\{&#37; endraw &#37;\} is determined by the locality-sensitivity properties of \{&#37; raw &#37;\}\\(\mathcal\{H\}\\)\{&#37; endraw &#37;\}. It follows from a recent result by Dahlgaard et al. (FOCS 2017) that the number of locality-sensitive hash functions can be reduced to \{&#37; raw &#37;\}\\(O(\log^2 n)\\)\{&#37; endraw &#37;\}, leaving the query time to be dominated by \{&#37; raw &#37;\}\\(O(n^\{\rho\})\\)\{&#37; endraw &#37;\} distance computations and \{&#37; raw &#37;\}\\(O(n^\{\rho\} \log n)\\)\{&#37; endraw &#37;\} additional word-RAM operations. We state this result as a general framework and provide a simpler analysis showing that the number of lookups and distance computations closely match the Indyk-Motwani framework, making it a viable replacement in practice. Using ideas from another locality-sensitive hashing framework by Andoni and Indyk (SODA 2006) we are able to reduce the number of additional word-RAM operations to \{&#37; raw &#37;\}\\(O(n^\rho)\\)\{&#37; endraw &#37;\}.
