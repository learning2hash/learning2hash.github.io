---
layout: publication
title: Parallel And Streaming Algorithms For K-core Decomposition
authors: Hossein Esfandiari, Silvio Lattanzi, Vahab Mirrokni
conference: Arxiv
year: 2018
bibkey: esfandiari2018parallel
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.02546'}]
tags: ["Efficiency", "Scalability"]
short_authors: Hossein Esfandiari, Silvio Lattanzi, Vahab Mirrokni
---
The \(k\)-core decomposition is a fundamental primitive in many machine
learning and data mining applications. We present the first distributed and the
first streaming algorithms to compute and maintain an approximate \(k\)-core
decomposition with provable guarantees. Our algorithms achieve rigorous bounds
on space complexity while bounding the number of passes or number of rounds of
computation. We do so by presenting a new powerful sketching technique for
\(k\)-core decomposition, and then by showing it can be computed efficiently in
both streaming and MapReduce models. Finally, we confirm the effectiveness of
our sketching technique empirically on a number of publicly available graphs.