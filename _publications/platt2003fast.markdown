---
layout: publication
title: Fast Embedding of Sparse Similarity Graphs
authors: John Platt
conference: "Neural Information Processing Systems"
year: 2003
bibkey: platt2003fast
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2003/hash/4e0223a87610176ef0d24ef6d2dcde3a-Abstract.html"}
tags: ['General', 'Graph', 'NEURIPS']
---
This paper applies fast sparse multidimensional scaling (MDS) to a large graph of music similarity with 267K vertices that represent artists al- bums and tracks; and 3.22M edges that represent similarity between those entities. Once vertices are assigned locations in a Euclidean space the locations can be used to browse music and to generate playlists. MDS on very large sparse graphs can be effectively performed by a family of algorithms called Rectangular Dijsktra (RD) MDS algorithms. These RD algorithms operate on a dense rectangular slice of the distance matrix created by calling Dijsktra a constant number of times. Two RD algorithms are compared Landmark MDS which uses the Nystr(cid246)m ap- proximation to perform MDS; and a new algorithm called Fast Sparse Embedding which uses FastMap. These algorithms compare favorably to Laplacian Eigenmaps both in terms of speed and embedding quality.
