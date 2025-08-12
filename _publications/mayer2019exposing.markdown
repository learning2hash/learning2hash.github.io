---
layout: publication
title: Exposing Fake Images With Forensic Similarity Graphs
authors: Owen Mayer, Matthew C. Stamm
conference: IEEE Journal of Selected Topics in Signal Processing
year: 2020
bibkey: mayer2019exposing
citations: 54
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.02861'}]
tags: []
short_authors: Owen Mayer, Matthew C. Stamm
---
We propose new image forgery detection and localization algorithms by
recasting these problems as graph-based community detection problems. To do
this, we introduce a novel abstract, graph-based representation of an image,
which we call the Forensic Similarity Graph, that captures key forensic
relationships among regions in the image. In this representation, small image
patches are represented by graph vertices with edges assigned according to the
forensic similarity between patches. Localized tampering introduces unique
structure into this graph, which aligns with a concept called ``community
structure'' in graph-theory literature. In the Forensic Similarity Graph,
communities correspond to the tampered and unaltered regions in the image. As a
result, forgery detection is performed by identifying whether multiple
communities exist, and forgery localization is performed by partitioning these
communities. We present two community detection techniques, adapted from
literature, to detect and localize image forgeries. We experimentally show that
our proposed community detection methods outperform existing state-of-the-art
forgery detection and localization methods, which do not capture such community
structure.