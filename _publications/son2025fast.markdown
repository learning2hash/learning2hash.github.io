---
layout: publication
title: 'FED: Fast And Efficient Dataset Deduplication Framework With GPU Acceleration'
authors: Youngjun Son, Chaewon Kim, Jaejin Lee
conference: Arxiv
year: 2025
citations: 0
bibkey: son2025fast
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.01046'}, {name: Code,
    url: 'https://github.com/mcrl/FED}{https://github.com/mcrl/FED})'}]
tags: [Tools and Libraries, Hashing Methods, Has Code]
---
Dataset deduplication plays a crucial role in enhancing data quality,
ultimately improving the training performance and efficiency of large language
models. A commonly used method for data deduplication is the MinHash LSH
algorithm. Recently, NVIDIA introduced a GPU-based MinHash LSH deduplication
method, but it remains suboptimal, leaving room for further improvement in
processing efficiency. This paper proposes a GPU-accelerated deduplication
framework, FED, that optimizes MinHash LSH for GPU clusters and leverages
computationally efficient, partially reusable non-cryptographic hash functions.
FED significantly outperforms the CPU-based deduplication tool in SlimPajama
(using 64 logical CPU cores) by up to 107.2 times and the GPU-based tool in
NVIDIA NeMo Curator by up to 6.3 times when processing 30 million documents on
a node with four GPUs. Notably, our method dramatically accelerates the
previously time-consuming MinHash signature generation phase, achieving
speed-ups of up to 260 compared to the CPU baseline. Despite these gains in
efficiency, FED maintains high deduplication quality, with the duplicate
document sets reaching a Jaccard similarity of over 0.96 compared to those
identified by the standard MinHash algorithm. In large-scale experiments, the
deduplication of 1.2 trillion tokens is completed in just 6 hours in a
four-node, 16-GPU environment. The related code is publicly available on GitHub
(\href\{https://github.com/mcrl/FED\}\{https://github.com/mcrl/FED\}).