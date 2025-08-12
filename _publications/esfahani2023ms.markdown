---
layout: publication
title: 'Ms-biographs: Sequence Similarity Graph Datasets'
authors: Mohsen Koohi Esfahani, Paolo Boldi, Hans Vandierendonck, Peter Kilpatrick,
  Sebastiano Vigna
conference: Arxiv
year: 2023
bibkey: esfahani2023ms
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.16744'}]
tags: ["Datasets"]
short_authors: Esfahani et al.
---
Progress in High-Performance Computing in general, and High-Performance Graph
Processing in particular, is highly dependent on the availability of
publicly-accessible, relevant, and realistic data sets.
  To ensure continuation of this progress, we (i) investigate and optimize the
process of generating large sequence similarity graphs as an HPC challenge and
(ii) demonstrate this process in creating MS-BioGraphs, a new family of
publicly available real-world edge-weighted graph datasets with up to \(2.5\)
trillion edges, that is, \(6.6\) times greater than the largest graph published
recently. The largest graph is created by matching (i.e., all-to-all similarity
aligning) \(1.7\) billion protein sequences. The MS-BioGraphs family includes
also seven subgraphs with different sizes and direction types.
  We describe two main challenges we faced in generating large graph datasets
and our solutions, that are, (i) optimizing data structures and algorithms for
this multi-step process and (ii) WebGraph parallel compression technique. We
present a comparative study of structural characteristics of MS-BioGraphs.
  The datasets are available online on
https://blogs.qub.ac.uk/DIPSA/MS-BioGraphs .