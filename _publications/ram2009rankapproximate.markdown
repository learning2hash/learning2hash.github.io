---
layout: publication
title: Rank-Approximate Nearest Neighbor Search Retaining Meaning and Speed in High Dimensions
authors: Parikshit Ram, Dongryeol Lee, Hua Ouyang, Alexander Gray
conference: "Neural Information Processing Systems"
year: 2009
bibkey: ram2009rankapproximate
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2009/hash/ddb30680a691d157187ee1cf9e896d03-Abstract.html"}
tags: ['General', 'NEURIPS']
---
The long-standing problem of efficient nearest-neighbor (NN) search has ubiquitous applications ranging from astrophysics to MP3 fingerprinting to bioinformatics to movie recommendations. As the dimensionality of the dataset increases exact NN search becomes computationally prohibitive; (1+eps)-distance-approximate NN search can provide large speedups but risks losing the meaning of NN search present in the ranks (ordering) of the distances. This paper presents a simple practical algorithm allowing the user to for the first time directly control the true accuracy of NN search (in terms of ranks) while still achieving the large speedups over exact NN. Experiments with high-dimensional datasets show that it often achieves faster and more accurate results than the best-known distance-approximate method with much more stable behavior.
