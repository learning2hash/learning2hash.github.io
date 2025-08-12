---
layout: publication
title: 'Locality Sensitive Hashing: A Comparison Of Hash Function Types And Querying
  Mechanisms'
authors: Loic Pauleve, Jegou, Amsaleg
conference: Pattern Recognition Letters
year: 2010
bibkey: pauleve2010locality
citations: 299
additional_links: [{name: Paper, url: 'https://hal.inria.fr/inria-00567191/document'}]
tags: ["Hashing Methods", "Locality Sensitive Hashing"]
short_authors: Loic Pauleve, Jegou, Amsaleg
---
It is well known that high-dimensional nearest-neighbor retrieval is very expensive. Dramatic performance gains are obtained using
approximate search schemes, such as the popular Locality-Sensitive Hashing (LSH). Several extensions have been proposed to
address the limitations of this algorithm, in particular, by choosing more appropriate hash functions to better partition the vector
space. All the proposed extensions, however, rely on a structured quantizer for hashing, poorly fitting real data sets, limiting
its performance in practice. In this paper, we compare several families of space hashing functions in a real setup, namely when
searching for high-dimension SIFT descriptors. The comparison of random projections, lattice quantizers, k-means and hierarchical
k-means reveal that unstructured quantizer significantly improves the accuracy of LSH, as it closely fits the data in the feature space.
We then compare two querying mechanisms introduced in the literature with the one originally proposed in LSH, and discuss their
respective merits and limitations.