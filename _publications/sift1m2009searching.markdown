---
layout: publication
title: "Searching with quantization: approximate nearest neighbor search using short codes and distance estimators"
authors: H. Jegou, M. Douze, C. Schmid
conference: INRIA Technical Report
year: 2009
bibkey: sift1m2009searching
additional_links:
   - {name: "PDF", url: "https://hal.inria.fr/inria-00410767/document/"}
   - {name: "URL", url: "http://corpus-texmex.irisa.fr/"}
   - {name: "Features", url: "https://www.dropbox.com/s/29f6r7pqevfy2ck/sift1m.mat?dl=0"}
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
