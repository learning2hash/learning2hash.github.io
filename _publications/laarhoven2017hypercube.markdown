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
A celebrated technique for finding near neighbors for the angular distance involves using a set of \textit{random} hyperplanes to partition the space into hash regions [Charikar, STOC 2002]. Experiments later showed that using a set of \textit{orthogonal} hyperplanes, thereby partitioning the space into the Voronoi regions induced by a hypercube, leads to even better results [Terasawa and Tanaka, WADS 2007]. However, no theoretical explanation for this improvement was ever given, and it remained unclear how the resulting hypercube hash method scales in high dimensions. In this work, we provide explicit asymptotics for the collision probabilities when using hypercubes to partition the space. For instance, two near-orthogonal vectors are expected to collide with probability \\((\frac&#123;1&#125;&#123;\pi&#125;)^&#123;d + o(d)&#125;\\) in dimension \\(d\\), compared to \\((\frac&#123;1&#125;&#123;2&#125;)^d\\) when using random hyperplanes. Vectors at angle \\(\frac&#123;\pi&#125;&#123;3&#125;\\) collide with probability \\((\frac&#123;\sqrt&#123;3&#125;&#125;&#123;\pi&#125;)^&#123;d + o(d)&#125;\\), compared to \\((\frac&#123;2&#125;&#123;3&#125;)^d\\) for random hyperplanes, and near-parallel vectors collide with similar asymptotic probabilities in both cases. For \\(c\\)-approximate nearest neighbor searching, this translates to a decrease in the exponent \\(\rho\\) of locality-sensitive hashing (LSH) methods of a factor up to \\(\log_2(\pi) \approx 1.652\\) compared to hyperplane LSH. For \\(c = 2\\), we obtain \\(\rho \approx 0.302 + o(1)\\) for hypercube LSH, improving upon the $\rho \approx 0.377$ for hyperplane LSH. We further describe how to use hypercube LSH in practice, and we consider an example application in the area of lattice algorithms.
