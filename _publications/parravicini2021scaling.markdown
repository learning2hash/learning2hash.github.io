---
layout: publication
title: Scaling Up HBM Efficiency Of Top-k Spmv For Approximate Embedding Similarity
  On Fpgas
authors: Alberto Parravicini, Luca Giuseppe Cellamare, Marco Siracusa, Marco Domenico
  Santambrogio
conference: 2021 58th ACM/IEEE Design Automation Conference (DAC)
year: 2021
bibkey: parravicini2021scaling
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.04808'}]
tags: [Efficiency, Evaluation]
short_authors: Parravicini et al.
---
Top-K SpMV is a key component of similarity-search on sparse embeddings. This
sparse workload does not perform well on general-purpose NUMA systems that
employ traditional caching strategies. Instead, modern FPGA accelerator cards
have a few tricks up their sleeve. We introduce a Top-K SpMV FPGA design that
leverages reduced precision and a novel packet-wise CSR matrix compression,
enabling custom data layouts and delivering bandwidth efficiency often
unreachable even in architectures with higher peak bandwidth. With HBM-based
boards, we are 100x faster than a multi-threaded CPU implementation and 2x
faster than a GPU with 20% higher bandwidth, with 14.2x higher
power-efficiency.