---
layout: publication
title: "Hashing with Graphs"
authors: W. Liu, J. Wang, S. Kumar, S. Chang
conference: ICML
year: 2011
bibkey: liu2011learning
additional_links:
   - {name: "PDF", url: "http://www.icml-2011.org/papers/6_icmlpaper.pdf"}
   - {name: "Code", url: "https://github.com/dengcai78/MatlabFunc/blob/master/ANNS/Hashing/Unsupervised/OneLayerAGH_Train.m"}
---
Hashing is becoming increasingly popular for
efficient nearest neighbor search in massive
databases. However, learning short codes
that yield good search performance is still
a challenge. Moreover, in many cases realworld
data lives on a low-dimensional manifold,
which should be taken into account
to capture meaningful nearest neighbors. In
this paper, we propose a novel graph-based
hashing method which automatically discovers
the neighborhood structure inherent in
the data to learn appropriate compact codes.
To make such an approach computationally
feasible, we utilize Anchor Graphs to obtain
tractable low-rank adjacency matrices. Our
formulation allows constant time hashing of a
new data point by extrapolating graph Laplacian
eigenvectors to eigenfunctions. Finally,
we describe a hierarchical threshold learning
procedure in which each eigenfunction yields
multiple bits, leading to higher search accuracy.
Experimental comparison with the
other state-of-the-art methods on two large
datasets demonstrates the efficacy of the proposed
method.
