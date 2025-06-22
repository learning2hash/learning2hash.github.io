---
layout: publication
title: Test-time Discovery Via Hashing Memory
authors: Fan Lyu, Tianle Liu, Zhang Zhang, Fuyuan Hu, Liang Wang
conference: Arxiv
year: 2025
citations: 0
bibkey: lyu2025test
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.10699'}, {name: Code,
    url: 'https://github.com/fanlyu/ttd'}]
tags: [Hashing Methods, Has Code]
---
We introduce Test-Time Discovery (TTD) as a novel task that addresses class
shifts during testing, requiring models to simultaneously identify emerging
categories while preserving previously learned ones. A key challenge in TTD is
distinguishing newly discovered classes from those already identified. To
address this, we propose a training-free, hash-based memory mechanism that
enhances class discovery through fine-grained comparisons with past test
samples. Leveraging the characteristics of unknown classes, our approach
introduces hash representation based on feature scale and directions, utilizing
Locality-Sensitive Hashing (LSH) for efficient grouping of similar samples.
This enables test samples to be easily and quickly compared with relevant past
instances. Furthermore, we design a collaborative classification strategy,
combining a prototype classifier for known classes with an LSH-based classifier
for novel ones. To enhance reliability, we incorporate a self-correction
mechanism that refines memory labels through hash-based neighbor retrieval,
ensuring more stable and accurate class assignments. Experimental results
demonstrate that our method achieves good discovery of novel categories while
maintaining performance on known classes, establishing a new paradigm in model
testing. Our code is available at https://github.com/fanlyu/ttd.