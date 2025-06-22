---
layout: publication
title: Topology-aware Hashing For Effective Control Flow Graph Similarity Analysis
authors: Yuping Li, Jiong Jang, Xinming Ou
conference: In International Conference on Security and Privacy in Communication Systems
  pp. 278-298. Springer Cham 2019
year: 2020
citations: 3
bibkey: li2020topology
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.06563'}]
tags: [Hashing Methods, ANN Search, Applications, Has Code]
---
Control Flow Graph (CFG) similarity analysis is an essential technique for a
variety of security analysis tasks, including malware detection and malware
clustering. Even though various algorithms have been developed, existing CFG
similarity analysis methods still suffer from limited efficiency, accuracy, and
usability. In this paper, we propose a novel fuzzy hashing scheme called
topology-aware hashing (TAH) for effective and efficient CFG similarity
analysis. Given the CFGs constructed from program binaries, we extract blended
n-gram graphical features of the CFGs, encode the graphical features into
numeric vectors (called graph signatures), and then measure the graph
similarity by comparing the graph signatures. We further employ a fuzzy hashing
technique to convert the numeric graph signatures into smaller fixed-size fuzzy
hash signatures for efficient similarity calculation. Our comprehensive
evaluation demonstrates that TAH is more effective and efficient compared to
existing CFG comparison techniques. To demonstrate the applicability of TAH to
real-world security analysis tasks, we develop a binary similarity analysis
tool based on TAH, and show that it outperforms existing similarity analysis
tools while conducting malware clustering.