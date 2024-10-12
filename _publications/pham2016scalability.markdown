---
layout: publication
title: Scalability And Total Recall With Fast Coveringlsh
authors: Pham Ninh, Pagh Rasmus
conference: "Arxiv"
year: 2016
bibkey: pham2016scalability
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1602.02620"}
tags: ['ARXIV', 'Independent', 'LSH']
---
Locality-sensitive hashing (LSH) has emerged as the dominant algorithmic technique for similarity search with strong performance guarantees in high-dimensional spaces. A drawback of traditional LSH schemes is that they may have \emph{false negatives}, i.e., the recall is less than 100\&#37;. This limits the applicability of LSH in settings requiring precise performance guarantees. Building on the recent theoretical CoveringLSH construction that eliminates false negatives, we propose a fast and practical covering LSH scheme for Hamming space called \emph{Fast CoveringLSH (fcLSH)}. Inheriting the design benefits of CoveringLSH our method avoids false negatives and always reports all near neighbors. Compared to CoveringLSH we achieve an asymptotic improvement to the hash function computation time from \\(\mathcal&#123;O&#125;(dL)\\) to \\(\mathcal&#123;O&#125;(d + L\log&#123;L&#125;)\\), where \\(d\\) is the dimensionality of data and \\(L\\) is the number of hash tables. Our experiments on synthetic and real-world data sets demonstrate that \emph{fcLSH} is comparable (and often superior) to traditional hashing-based approaches for search radius up to 20 in high-dimensional Hamming space.
