---
layout: publication
title: 'Sketching And Sequence Alignment: A Rate-distortion Perspective'
authors: Ilan Shomorony, Govinda M. Kamath
conference: 2021 IEEE International Symposium on Information Theory (ISIT)
year: 2021
bibkey: shomorony2021sketching
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.04202'}]
tags: ["Hashing Methods", "Tools & Libraries"]
short_authors: Ilan Shomorony, Govinda M. Kamath
---
Pairwise alignment of DNA sequencing data is a ubiquitous task in
bioinformatics and typically represents a heavy computational burden. A
standard approach to speed up this task is to compute "sketches" of the DNA
reads (typically via hashing-based techniques) that allow the efficient
computation of pairwise alignment scores. We propose a rate-distortion
framework to study the problem of computing sketches that achieve the optimal
tradeoff between sketch size and alignment estimation distortion. We consider
the simple setting of i.i.d. error-free sources of length \(n\) and introduce a
new sketching algorithm called "locational hashing." While standard approaches
in the literature based on min-hashes require \(B = (1/D) \cdot O\left( log n
\right)\) bits to achieve a distortion \(D\), our proposed approach only requires
\(B = log^2(1/D) \cdot O(1)\) bits. This can lead to significant computational
savings in pairwise alignment estimation.