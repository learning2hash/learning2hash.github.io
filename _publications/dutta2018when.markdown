---
layout: publication
title: 'When Hashing Met Matching: Efficient Spatio-temporal Search For Ridesharing'
authors: Chinmoy Dutta
conference: "Arxiv"
year: 2018
citations: 6
bibkey: dutta2018when
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1809.02680'}
tags: ['Independent', 'Unimodal', 'Shallow', 'Datasets', 'Training Strategy', 'Hashing']
---
Carpooling, or sharing a ride with other passengers, holds immense potential
for urban transportation. Ridesharing platforms enable such sharing of rides
using real-time data. Finding ride matches in real-time at urban scale is a
difficult combinatorial optimization task and mostly heuristic approaches are
applied. In this work, we mathematically model the problem as that of finding
near-neighbors and devise a novel efficient spatio-temporal search algorithm
based on the theory of locality sensitive hashing for Maximum Inner Product
Search (MIPS). The proposed algorithm can find \\(k\\) near-optimal potential
matches for every ride from a pool of \\(n\\) rides in time \\(O(n^\{1 + \rho\} (k +
log n) log k)\\) and space \\(O(n^\{1 + \rho\} log k)\\) for a small \\(\rho < 1\\). Our
algorithm can be extended in several useful and interesting ways increasing its
practical appeal. Experiments with large NY yellow taxi trip datasets show that
our algorithm consistently outperforms state-of-the-art heuristic methods
thereby proving its practical applicability.
