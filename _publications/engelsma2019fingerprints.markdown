---
layout: publication
title: 'Fingerprints: Fixed Length Representation Via Deep Networks And Domain Knowledge'
authors: Engelsma Joshua J., Cao Kai, Jain Anil K.
conference: Arxiv
year: 2019
bibkey: engelsma2019fingerprints
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.01099'}]
tags: ["Compact Codes", "Distance Metric Learning", "Hashing Methods", "Neural Hashing", "Quantization", "Similarity Search"]
short_authors: Engelsma Joshua J., Cao Kai, Jain Anil K.
---
We learn a discriminative fixed length feature representation of fingerprints
which stands in contrast to commonly used unordered, variable length sets of
minutiae points. To arrive at this fixed length representation, we embed
fingerprint domain knowledge into a multitask deep convolutional neural network
architecture. Empirical results, on two public-domain fingerprint databases
(NIST SD4 and FVC 2004 DB1) show that compared to minutiae representations,
extracted by two state-of-the-art commercial matchers (Verifinger v6.3 and
Innovatrics v2.0.3), our fixed-length representations provide (i) higher search
accuracy: Rank-1 accuracy of 97.9% vs. 97.3% on NIST SD4 against a gallery size
of 2000 and (ii) significantly faster, large scale search: 682,594 matches per
second vs. 22 matches per second for commercial matchers on an i5 3.3 GHz
processor with 8 GB of RAM.