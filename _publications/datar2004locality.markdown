---
layout: publication
title: "Locality-sensitive hashing scheme based on p-stable distributions"
authors: M. Datar, N. Immorlica, P. Indyk, V. Mirrokni
conference: SCG
year: 2004
bibkey: datar2004locality
additional_links:
   - {name: "PDF", url: "https://dl.acm.org/citation.cfm?id=997857"}
   - {name: "Code", url: "http://www.mit.edu/~andoni/LSH/"}
   - {name: "Tutorial", url: "http://www.slaney.org/malcolm/yahoo/Slaney2008-LSHTutorial.pdf"}
---
We present a novel Locality-Sensitive Hashing scheme for the Approximate Nearest Neighbor Problem under lp norm, based on p-stable distributions.Our scheme improves the running time of the earlier algorithm for the case of the lp norm. It also yields the first known provably efficient approximate NN algorithm for the case p<1. We also show that the algorithm finds the exact near neigbhor in O(log n) time for data satisfying certain "bounded growth" condition.Unlike earlier schemes, our LSH scheme works directly on points in the Euclidean space without embeddings. Consequently, the resulting query time bound is free of large factors and is simple and easy to implement. Our experiments (on synthetic data sets) show that the our data structure is up to 40 times faster than kd-tree.
