---
layout: publication
title: Clustering Is Efficient For Approximate Maximum Inner Product Search
authors: Auvolat Alex, Chandar Sarath, Vincent Pascal, Larochelle Hugo, Bengio Yoshua
conference: "Arxiv"
year: 2015
bibkey: auvolat2015clustering
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1507.05910"}
tags: ['ARXIV', 'LSH', 'Unsupervised']
---
Efficient Maximum Inner Product Search (MIPS) is an important task that has a wide applicability in recommendation systems and classification with a large number of classes. Solutions based on locality45;sensitive hashing (LSH) as well as tree45;based solutions have been investigated in the recent literature to perform approximate MIPS in sublinear time. In this paper we compare these to another extremely simple approach for solving approximate MIPS based on variants of the k45;means clustering algorithm. Specifically we propose to train a spherical k45;means after having reduced the MIPS problem to a Maximum Cosine Similarity Search (MCSS). Experiments on two standard recommendation system benchmarks as well as on large vocabulary word embeddings show that this simple approach yields much higher speedups for the same retrieval precision than current state45;of45;the45;art hashing45;based and tree45;based methods. This simple method also yields more robust retrievals when the query is corrupted by noise.
