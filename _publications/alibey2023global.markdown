---
layout: publication
title: Global Proxy-based Hard Mining For Visual Place Recognition
authors: "Amar Ali-Bey, Brahim Chaib-Draa, Philippe Gigu\xE8re"
conference: Arxiv
year: 2023
bibkey: alibey2023global
citations: 1
additional_links: [{name: Code, url: 'https://github.com/amaralibey/GPM'}, {name: Paper,
    url: 'https://arxiv.org/abs/2302.14217'}]
tags: ["Datasets", "Evaluation", "Scalability"]
short_authors: "Amar Ali-Bey, Brahim Chaib-Draa, Philippe Gigu\xE8re"
---
Learning deep representations for visual place recognition is commonly
performed using pairwise or triple loss functions that highly depend on the
hardness of the examples sampled at each training iteration. Existing
techniques address this by using computationally and memory expensive offline
hard mining, which consists of identifying, at each iteration, the hardest
samples from the training set. In this paper we introduce a new technique that
performs global hard mini-batch sampling based on proxies. To do so, we add a
new end-to-end trainable branch to the network, which generates efficient place
descriptors (one proxy for each place). These proxy representations are thus
used to construct a global index that encompasses the similarities between all
places in the dataset, allowing for highly informative mini-batch sampling at
each training iteration. Our method can be used in combination with all
existing pairwise and triplet loss functions with negligible additional memory
and computation cost. We run extensive ablation studies and show that our
technique brings new state-of-the-art performance on multiple large-scale
benchmarks such as Pittsburgh, Mapillary-SLS and SPED. In particular, our
method provides more than 100% relative improvement on the challenging Nordland
dataset. Our code is available at https://github.com/amaralibey/GPM