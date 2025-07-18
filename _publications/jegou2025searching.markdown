---
layout: publication
title: 'Searching With Quantization: Approximate Nearest Neighbor Search Using Short
  Codes And Distance Estimators'
authors: Jegou H., Douze, Schmid
conference: No Venue
year: 2025
bibkey: jegou2025searching
citations: 17
additional_links: [{name: Paper, url: 'https://hal.inria.fr/inria-00410767/document/'}]
tags: [Compact Codes, Hashing Methods, Quantization, Distance Metric Learning]
---
We propose an approximate nearest neighbor search method based
on quantization. It uses, in particular, product quantizer to produce short codes
and corresponding distance estimators approximating the Euclidean distance
between the orginal vectors. The method is advantageously used in an asymmetric
manner, by computing the distance between a vector and code, unlike
competing techniques such as spectral hashing that only compare codes.
Our approach approximates the Euclidean distance based on memory efficient codes and, thus, permits efficient nearest neighbor search. Experiments
performed on SIFT and GIST image descriptors show excellent search accuracy.
The method is shown to outperform two state-of-the-art approaches of the literature.
Timings measured when searching a vector set of 2 billion vectors are
shown to be excellent given the high accuracy of the method.