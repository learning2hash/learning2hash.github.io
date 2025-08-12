---
layout: publication
title: Faster Batched Range Minimum Queries
authors: Szymon Grabowski, Tomasz Kowalski
conference: Arxiv
year: 2017
bibkey: grabowski2017faster
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.06940'}]
tags: ["Efficiency", "Scalability"]
short_authors: Szymon Grabowski, Tomasz Kowalski
---
Range Minimum Query (RMQ) is an important building brick of many compressed
data structures and string matching algorithms. Although this problem is
essentially solved in theory, with sophisticated data structures allowing for
constant time queries, there are scenarios in which the number of queries, \(q\),
is rather small and given beforehand, which encourages to use a simpler
approach. A recent work by Alzamel et al. starts with contracting the input
array to a much shorter one, with its size proportional to \(q\). In this work,
we build upon their solution, speeding up handling small batches of queries by
a factor of 3.8--7.8 (the gap grows with \(q\)). The key idea that helped us
achieve this advantage is adapting the well-known Sparse Table technique to
work on blocks, with speculative block minima comparisons. We also propose an
even much faster (but possibly using more space) variant without the array
contraction.