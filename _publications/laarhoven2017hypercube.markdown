---
layout: publication
title: Hypercube LSH For Approximate Near Neighbors
authors: Laarhoven Thijs
conference: ""
year: 2017
bibkey: laarhoven2017hypercube
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1702.05760"}
tags: ['Independent', 'LSH']
---
A celebrated technique for finding near neighbors for the angular distance involves using a set of \textit&amp;\#123;random&amp;\#125; hyperplanes to partition the space into hash regions [Charikar, STOC 2002]. Experiments later showed that using a set of \textit&amp;\#123;orthogonal&amp;\#125; hyperplanes, thereby partitioning the space into the Voronoi regions induced by a hypercube, leads to even better results [Terasawa and Tanaka, WADS 2007]. However, no theoretical explanation for this improvement was ever given, and it remained unclear how the resulting hypercube hash method scales in high dimensions. In this work, we provide explicit asymptotics for the collision probabilities when using hypercubes to partition the space. For instance, two near-orthogonal vectors are expected to collide with probability \((\frac\&amp;\#123;1\&amp;\#125;\&amp;\#123;\pi\&amp;\#125;)^\&amp;\#123;d + o(d)\&amp;\#125;\) in dimension \(d\), compared to \((\frac\&amp;\#123;1\&amp;\#125;\&amp;\#123;2\&amp;\#125;)^d\) when using random hyperplanes. Vectors at angle \(\frac\&amp;\#123;\pi\&amp;\#125;\&amp;\#123;3\&amp;\#125;\) collide with probability \((\frac\&amp;\#123;\sqrt\&amp;\#123;3\&amp;\#125;\&amp;\#125;\&amp;\#123;\pi\&amp;\#125;)^\&amp;\#123;d + o(d)\&amp;\#125;\), compared to \((\frac\&amp;\#123;2\&amp;\#125;\&amp;\#123;3\&amp;\#125;)^d\) for random hyperplanes, and near-parallel vectors collide with similar asymptotic probabilities in both cases. For \(c\)-approximate nearest neighbor searching, this translates to a decrease in the exponent \(\rho\) of locality-sensitive hashing (LSH) methods of a factor up to \(\log\_2(\pi) \approx 1.652\) compared to hyperplane LSH. For \(c = 2\), we obtain \(\rho \approx 0.302 + o(1)\) for hypercube LSH, improving upon the $\rho \approx 0.377$ for hyperplane LSH. We further describe how to use hypercube LSH in practice, and we consider an example application in the area of lattice algorithms.
