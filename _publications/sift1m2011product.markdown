---
layout: publication
title: "Product quantization for nearest neighbor search"
authors: H. Jegou, M. Douze, C. Schmid
conference: TPAMI
year: 2011
bibkey: sift1m2011product
additional_links:
   - {name: "URL", url: "http://corpus-texmex.irisa.fr/"}
   - {name: "Features", url: "https://www.dropbox.com/s/29f6r7pqevfy2ck/sift1m.mat?dl=0"}
---
Overview: This page provides several evaluation sets to evaluate the quality of approximate 
nearest neighbors search algorithm on different kinds of data and varying database sizes. 
In particular, we provide a very large set of 1 billion vectors, to our knowledge 
this is the largest set provided to evaluate ANN methods. Each comprises 3 subsets of vectors:

* base vectors: the vectors in which the search is performed
* query vectors
* learning vectors: to find the parameters involved in a particular method

In addition, we provide the groundtruth for each set, in the form of the pre-computed k nearest neighbors and their square Euclidean distance. 
