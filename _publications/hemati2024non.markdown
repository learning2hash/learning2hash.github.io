---
layout: publication
title: A Non-alternating Graph Hashing Algorithm For Large Scale Image Search
authors: Hemati Sobhan, Mehdizavareh, Chenouri, Tizhoosh
conference: "Arxiv"
year: 2024
bibkey: hemati2024non
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2012.13138"}
tags: ['ARXIV', 'Graph']
---
<p>In the era of big data, methods for improving memory and
computational efficiency have become crucial for successful deployment
of technologies. Hashing is one of the most effective approaches to deal
with computational limitations that come with big data. One natural way
for formulating this problem is spectral hashing that directly
incorporates affinity to learn binary codes. However, due to binary
constraints, the optimization becomes intractable. To mitigate this
challenge, different relaxation approaches have been proposed to reduce
the computational load of obtaining binary codes and still attain a good
solution. The problem with all existing relaxation methods is resorting
to one or more additional auxiliary variables to attain high quality
binary codes while relaxing the problem. The existence of auxiliary
variables leads to coordinate descent approach which increases the
computational complexity. We argue that introducing these variables is
unnecessary. To this end, we propose a novel relaxed formulation for
spectral hashing that adds no additional variables to the problem.
Furthermore, instead of solving the problem in original space where
number of variables is equal to the data points, we solve the problem in
a much smaller space and retrieve the binary codes from this solution.
This trick reduces both the memory and computational complexity at the
same time. We apply two optimization techniques, namely projected
gradient and optimization on manifold, to obtain the solution. Using
comprehensive experiments on four public datasets, we show that the
proposed efficient spectral hashing (ESH) algorithm achieves highly
competitive retrieval performance compared with state of the art at low
complexity.</p>
