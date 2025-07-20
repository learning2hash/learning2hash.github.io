---
layout: publication
title: Accelerating Large-Scale Inference with Anisotropic Vector Quantization
authors: Guo et al.
conference: Arxiv
year: 2019
bibkey: guo2019accelerating
citations: 91
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.10396'}]
tags: [Quantization, SCALABILITY]
---
Quantization based techniques are the current state-of-the-art for scaling
maximum inner product search to massive databases. Traditional approaches to
quantization aim to minimize the reconstruction error of the database points.
Based on the observation that for a given query, the database points that have
the largest inner products are more relevant, we develop a family of
anisotropic quantization loss functions. Under natural statistical assumptions,
we show that quantization with these loss functions leads to a new variant of
vector quantization that more greatly penalizes the parallel component of a
datapoint's residual relative to its orthogonal component. The proposed
approach achieves state-of-the-art results on the public benchmarks available
at \url\{ann-benchmarks.com\}.