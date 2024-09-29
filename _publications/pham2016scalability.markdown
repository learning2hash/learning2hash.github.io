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
Locality45;sensitive hashing (LSH) has emerged as the dominant algorithmic technique for similarity search with strong performance guarantees in high45;dimensional spaces. A drawback of traditional LSH schemes is that they may have emph123;false negatives125; i.e. the recall is less than 10037;. This limits the applicability of LSH in settings requiring precise performance guarantees. Building on the recent theoretical CoveringLSH construction that eliminates false negatives we propose a fast and practical covering LSH scheme for Hamming space called emph123;Fast CoveringLSH (fcLSH)125;. Inheriting the design benefits of CoveringLSH our method avoids false negatives and always reports all near neighbors. Compared to CoveringLSH we achieve an asymptotic improvement to the hash function computation time from mathcal123;O125;(dL) to mathcal123;O125;(d + Llog123;L125;) where d is the dimensionality of data and L is the number of hash tables. Our experiments on synthetic and real45;world data sets demonstrate that emph123;fcLSH125; is comparable (and often superior) to traditional hashing45;based approaches for search radius up to 20 in high45;dimensional Hamming space.
