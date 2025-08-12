---
layout: publication
title: Fast And Lightweight Distributed Suffix Array Construction -- First Results
authors: Manuel Haag, Florian Kurpicz, Peter Sanders, Matthias Schimek
conference: Arxiv
year: 2024
bibkey: haag2024fast
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.10160'}]
tags: ["Efficiency", "Scalability"]
short_authors: Haag et al.
---
We present first algorithmic ideas for a practical and lightweight adaption
of the DCX suffix array construction algorithm [Sanders et al., 2003] to the
distributed-memory setting. Our approach relies on a bucketing technique which
enables a lightweight implementation which uses less than half of the memory
required by the currently fastest distributed-memory suffix array algorithm
PSAC [Flick and Aluru, 2015] while being competitive or even faster in terms of
running time.