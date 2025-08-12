---
layout: publication
title: Fast Graph Kernel With Optical Random Features
authors: Hashem Ghanem, Nicolas Keriven, Nicolas Tremblay
conference: ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2021
bibkey: ghanem2020fast
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.08270'}]
tags: ["ICASSP"]
short_authors: Hashem Ghanem, Nicolas Keriven, Nicolas Tremblay
---
The graphlet kernel is a classical method in graph classification. It however
suffers from a high computation cost due to the isomorphism test it includes.
As a generic proxy, and in general at the cost of losing some information, this
test can be efficiently replaced by a user-defined mapping that computes
various graph characteristics. In this paper, we propose to leverage kernel
random features within the graphlet framework, and establish a theoretical link
with a mean kernel metric. If this method can still be prohibitively costly for
usual random features, we then incorporate optical random features that can be
computed in constant time. Experiments show that the resulting algorithm is
orders of magnitude faster that the graphlet kernel for the same, or better,
accuracy.