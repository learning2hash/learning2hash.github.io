---
layout: publication
title: Proximity Preserving Binary Code Using Signed Graph-cut
authors: Inbal Lav, Shai Avidan, Yoram Singer, Yacov Hel-Or
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2020
bibkey: lav2020proximity
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.01793'}]
tags: [Hashing Methods, Compact Codes, Tools & Libraries, AAAI]
short_authors: Lav et al.
---
We introduce a binary embedding framework, called Proximity Preserving Code
(PPC), which learns similarity and dissimilarity between data points to create
a compact and affinity-preserving binary code. This code can be used to apply
fast and memory-efficient approximation to nearest-neighbor searches. Our
framework is flexible, enabling different proximity definitions between data
points. In contrast to previous methods that extract binary codes based on
unsigned graph partitioning, our system models the attractive and repulsive
forces in the data by incorporating positive and negative graph weights. The
proposed framework is shown to boil down to finding the minimal cut of a signed
graph, a problem known to be NP-hard. We offer an efficient approximation and
achieve superior results by constructing the code bit after bit. We show that
the proposed approximation is superior to the commonly used spectral methods
with respect to both accuracy and complexity. Thus, it is useful for many other
problems that can be translated into signed graph cut.