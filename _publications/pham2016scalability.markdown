---
layout: publication
title: Scalability And Total Recall With Fast Coveringlsh
authors: Pham Ninh, Pagh Rasmus
conference: Proceedings of the 25th ACM International on Conference on Information
  and Knowledge Management
year: 2016
bibkey: pham2016scalability
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.02620'}]
tags: ["Hashing-Methods", "Locality-Sensitive-Hashing", "CIKM", "Similarity-Search", "Scalability", "Evaluation"]
short_authors: Pham Ninh, Pagh Rasmus
---
Locality-sensitive hashing (LSH) has emerged as the dominant algorithmic
technique for similarity search with strong performance guarantees in
high-dimensional spaces. A drawback of traditional LSH schemes is that they may
have *false negatives*, i.e., the recall is less than 100%. This limits
the applicability of LSH in settings requiring precise performance guarantees.
Building on the recent theoretical "CoveringLSH" construction that eliminates
false negatives, we propose a fast and practical covering LSH scheme for
Hamming space called *Fast CoveringLSH (fcLSH)*. Inheriting the design
benefits of CoveringLSH our method avoids false negatives and always reports
all near neighbors. Compared to CoveringLSH we achieve an asymptotic
improvement to the hash function computation time from \\(\mathcal\{O\}(dL)\\) to
\\(\mathcal\{O\}(d + Llog\{L\})\\), where \\(d\\) is the dimensionality of data and \\(L\\) is
the number of hash tables. Our experiments on synthetic and real-world data
sets demonstrate that *fcLSH* is comparable (and often superior) to
traditional hashing-based approaches for search radius up to 20 in
high-dimensional Hamming space.