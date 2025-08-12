---
layout: publication
title: 'Probgraph: High-performance And High-accuracy Graph Mining With Probabilistic
  Set Representations'
authors: "MacIej Besta, Cesare Miglioli, Paolo Sylos Labini, Jakub T\u011Btek, Patrick\
  \ Iff, Raghavendra Kanakagiri, Saleh Ashkboos, Kacper Janda, Michal Podstawski,\
  \ Grzegorz Kwasniewski, Niels Gleinig, Flavio Vella, Onur Mutlu, Torsten Hoefler"
conference: 'SC22: International Conference for High Performance Computing, Networking,
  Storage and Analysis'
year: 2022
bibkey: besta2022probgraph
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.11469'}]
tags: []
short_authors: Besta et al.
---
Important graph mining problems such as Clustering are computationally
demanding. To significantly accelerate these problems, we propose ProbGraph: a
graph representation that enables simple and fast approximate parallel graph
mining with strong theoretical guarantees on work, depth, and result accuracy.
The key idea is to represent sets of vertices using probabilistic set
representations such as Bloom filters. These representations are much faster to
process than the original vertex sets thanks to vectorizability and small size.
We use these representations as building blocks in important parallel graph
mining algorithms such as Clique Counting or Clustering. When enhanced with
ProbGraph, these algorithms significantly outperform tuned parallel exact
baselines (up to nearly 50x on 32 cores) while ensuring accuracy of more than
90% for many input graph datasets. Our novel bounds and algorithms based on
probabilistic set representations with desirable statistical properties are of
separate interest for the data analytics community.