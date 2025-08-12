---
layout: publication
title: 'Dodo-code: A Deep Levenshtein Distance Embedding-based Code For IDS Channel
  And DNA Storage'
authors: Alan J. X. Guo, Sihan Sun, Xiang Wei, Mengyi Wei, Xin Chen
conference: Arxiv
year: 2023
bibkey: guo2023dodo
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.12717'}]
tags: ["Efficiency", "Neural Hashing"]
short_authors: Guo et al.
---
Recently, DNA storage has emerged as a promising data storage solution,
offering significant advantages in storage density, maintenance cost
efficiency, and parallel replication capability. Mathematically, the DNA
storage pipeline can be viewed as an insertion, deletion, and substitution
(IDS) channel. Because of the mathematical terra incognita of the Levenshtein
distance, designing an IDS-correcting code is still a challenge. In this paper,
we propose an innovative approach that utilizes deep Levenshtein distance
embedding to bypass these mathematical challenges. By representing the
Levenshtein distance between two sequences as a conventional distance between
their corresponding embedding vectors, the inherent structural property of
Levenshtein distance is revealed in the friendly embedding space. Leveraging
this embedding space, we introduce the DoDo-Code, an IDS-correcting code that
incorporates deep embedding of Levenshtein distance, deep embedding-based
codeword search, and deep embedding-based segment correcting. To address the
requirements of DNA storage, we also present a preliminary algorithm for long
sequence decoding. As far as we know, the DoDo-Code is the first IDS-correcting
code designed using plausible deep learning methodologies, potentially paving
the way for a new direction in error-correcting code research. It is also the
first IDS code that exhibits characteristics of being `optimal' in terms of
redundancy, significantly outperforming the mainstream IDS-correcting codes of
the Varshamov-Tenengolts code family in code rate.