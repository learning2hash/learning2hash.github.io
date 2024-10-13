---
layout: publication
title: Proximity Preserving Binary Code Using Signed Graph-cut
authors: Lav Inbal, Avidan Shai, Singer Yoram, Hel-or Yacov
conference: "AAAI Conference on Artificial Intelligence Feb."
year: 2020
bibkey: lav2020proximity
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2002.01793"}
tags: ['Graph']
---
<p>We introduce a binary embedding framework, called Proximity
Preserving Code (PPC), which learns similarity and dissimilarity between
data points to create a compact and affinity-preserving binary code.
This code can be used to apply fast and memory-efficient approximation
to nearest-neighbor searches. Our framework is flexible, enabling
different proximity definitions between data points. In contrast to
previous methods that extract binary codes based on unsigned graph
partitioning, our system models the attractive and repulsive forces in
the data by incorporating positive and negative graph weights. The
proposed framework is shown to boil down to finding the minimal cut of a
signed graph, a problem known to be NP-hard. We offer an efficient
approximation and achieve superior results by constructing the code bit
after bit. We show that the proposed approximation is superior to the
commonly used spectral methods with respect to both accuracy and
complexity. Thus, it is useful for many other problems that can be
translated into signed graph cut.</p>
