---
layout: publication
title: 'Latent Fingerprint Recognition: Role Of Texture Template'
authors: Kai Cao, Anil K. Jain
conference: 2018 IEEE 9th International Conference on Biometrics Theory, Applications
  and Systems (BTAS)
year: 2018
bibkey: cao2018latent
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.10337'}]
tags: []
short_authors: Kai Cao, Anil K. Jain
---
We propose a texture template approach, consisting of a set of virtual
minutiae, to improve the overall latent fingerprint recognition accuracy. To
compensate for the lack of sufficient number of minutiae in poor quality latent
prints, we generate a set of virtual minutiae. However, due to a large number
of these regularly placed virtual minutiae, texture based template matching has
a large computational requirement compared to matching true minutiae templates.
To improve both the accuracy and efficiency of the texture template matching,
we investigate: i) both original and enhanced fingerprint patches for training
convolutional neural networks (ConvNets) to improve the distinctiveness of
descriptors associated with each virtual minutiae, ii) smaller patches around
virtual minutiae and a fast ConvNet architecture to speed up descriptor
extraction, iii) reduce the descriptor length, iv) a modified hierarchical
graph matching strategy to improve the matching speed, and v) extraction of
multiple texture templates to boost the performance. Experiments on NIST SD27
latent database show that the above strategies can improve the matching speed
from 11 ms (24 threads) per comparison (between a latent and a reference print)
to only 7.7 ms (single thread) per comparison while improving the rank-1
accuracy by 8.9% against 10K gallery.