---
layout: publication
title: Improved Residual Vector Quantization For High-dimensional Approximate Nearest
  Neighbor Search
authors: Shicong Liu, Hongtao Lu, Junru Shao
conference: Arxiv
year: 2015
citations: 2
bibkey: liu2015improved
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1509.05195'}]
tags: [Quantization, ANN Search, Evaluation Metrics, Benchmarks and Datasets, Has
    Code]
---
Quantization methods have been introduced to perform large scale approximate
nearest search tasks. Residual Vector Quantization (RVQ) is one of the
effective quantization methods. RVQ uses a multi-stage codebook learning scheme
to lower the quantization error stage by stage. However, there are two major
limitations for RVQ when applied to on high-dimensional approximate nearest
neighbor search: 1. The performance gain diminishes quickly with added stages.
2. Encoding a vector with RVQ is actually NP-hard. In this paper, we propose an
improved residual vector quantization (IRVQ) method, our IRVQ learns codebook
with a hybrid method of subspace clustering and warm-started k-means on each
stage to prevent performance gain from dropping, and uses a multi-path encoding
scheme to encode a vector with lower distortion. Experimental results on the
benchmark datasets show that our method gives substantially improves RVQ and
delivers better performance compared to the state-of-the-art.