---
layout: publication
title: 'Retsim: Resilient And Efficient Text Similarity'
authors: Marina Zhang, Owen Vallis, Aysegul Bumin, Tanay Vakharia, Elie Bursztein
conference: Arxiv
year: 2023
bibkey: zhang2023retsim
citations: 0
additional_links: [{name: Code, url: 'https://github.com/google/unisim.'}, {name: Paper,
    url: 'https://arxiv.org/abs/2311.17264'}]
tags: ["Datasets", "Evaluation", "Locality-Sensitive-Hashing", "Neural Hashing", "Robustness", "Text Retrieval"]
short_authors: Zhang et al.
---
This paper introduces RETSim (Resilient and Efficient Text Similarity), a
lightweight, multilingual deep learning model trained to produce robust metric
embeddings for near-duplicate text retrieval, clustering, and dataset
deduplication tasks. We demonstrate that RETSim is significantly more robust
and accurate than MinHash and neural text embeddings, achieving new
state-of-the-art performance on dataset deduplication, adversarial text
retrieval benchmarks, and spam clustering tasks. We also introduce the W4NT3D
benchmark (Wiki-40B 4dversarial Near-T3xt Dataset) for evaluating multilingual,
near-duplicate text retrieval capabilities under adversarial settings. RETSim
and the W4NT3D benchmark are open-sourced under the MIT License at
https://github.com/google/unisim.