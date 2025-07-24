---
layout: publication
title: Sub-linear Privacy-preserving Near-neighbor Search
authors: M. Sadegh Riazi, Beidi Chen, Anshumali Shrivastava, Dan Wallach, Farinaz
  Koushanfar
conference: Arxiv
year: 2016
bibkey: riazi2016sub
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.01835'}]
tags: ["Efficiency", "Hashing Methods", "Locality Sensitive Hashing", "Privacy & Security"]
short_authors: Riazi et al.
---
In Near-Neighbor Search (NNS), a new client queries a database (held by a
server) for the most similar data (near-neighbors) given a certain similarity
metric. The Privacy-Preserving variant (PP-NNS) requires that neither server
nor the client shall learn information about the other party's data except what
can be inferred from the outcome of NNS. The overwhelming growth in the size of
current datasets and the lack of a truly secure server in the online world
render the existing solutions impractical; either due to their high
computational requirements or non-realistic assumptions which potentially
compromise privacy. PP-NNS having query time \{\it sub-linear\} in the size of
the database has been suggested as an open research direction by Li et al.
(CCSW'15). In this paper, we provide the first such algorithm, called Secure
Locality Sensitive Indexing (SLSI) which has a sub-linear query time and the
ability to handle honest-but-curious parties. At the heart of our proposal lies
a secure binary embedding scheme generated from a novel probabilistic
transformation over locality sensitive hashing family. We provide information
theoretic bound for the privacy guarantees and support our theoretical claims
using substantial empirical evidence on real-world datasets.