---
layout: publication
title: "Practical and Optimal LSH for Angular Distance"
authors: A. Andoni, P. Indyk, T. Laarhoven
conference: NIPS
year: 2015
bibkey: andoni2015practical
additional_links:
   - {name: "PDF", url: "https://papers.nips.cc/paper/5893-practical-and-optimal-lsh-for-angular-distance.pdf"}
   - {name: "Code", url: "http://www.mit.edu/~andoni/LSH/"}
   - {name: "Tutorial", url: "https://people.csail.mit.edu/indyk/p117-andoni.pdf"}
---
We show the existence of a Locality-Sensitive Hashing (LSH) family for the angular
distance that yields an approximate Near Neighbor Search algorithm with the
asymptotically optimal running time exponent. Unlike earlier algorithms with this
property (e.g., Spherical LSH [1, 2]), our algorithm is also practical, improving
upon the well-studied hyperplane LSH [3] in practice. We also introduce a multiprobe
version of this algorithm and conduct an experimental evaluation on real
and synthetic data sets.
We complement the above positive results with a fine-grained lower bound for the
quality of any LSH family for angular distance. Our lower bound implies that the
above LSH family exhibits a trade-off between evaluation time and quality that is
close to optimal for a natural class of LSH functions.
