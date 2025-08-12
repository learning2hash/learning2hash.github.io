---
layout: publication
title: Accelerating Local Search For The Maximum Independent Set Problem
authors: Jakob Dahlum, Sebastian Lamm, Peter Sanders, Christian Schulz, Darren Strash,
  Renato F. Werneck
conference: Lecture Notes in Computer Science
year: 2016
bibkey: dahlum2016accelerating
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.01659'}]
tags: []
short_authors: Dahlum et al.
---
Computing high-quality independent sets quickly is an important problem in
combinatorial optimization. Several recent algorithms have shown that
kernelization techniques can be used to find exact maximum independent sets in
medium-sized sparse graphs, as well as high-quality independent sets in huge
sparse graphs that are intractable for exact (exponential-time) algorithms.
However, a major drawback of these algorithms is that they require significant
preprocessing overhead, and therefore cannot be used to find a high-quality
independent set quickly.
  In this paper, we show that performing simple kernelization techniques in an
online fashion significantly boosts the performance of local search, and is
much faster than pre-computing a kernel using advanced techniques. In addition,
we show that cutting high-degree vertices can boost local search performance
even further, especially on huge (sparse) complex networks. Our experiments
show that we can drastically speed up the computation of large independent sets
compared to other state-of-the-art algorithms, while also producing results
that are very close to the best known solutions.