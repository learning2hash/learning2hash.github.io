---
layout: publication
title: Aisaq All-in-storage ANNS With Product Quantization For Dram-free Information
  Retrieval
authors: Tatsuno Kento et al.
conference: Arxiv
year: 2024
citations: 0
bibkey: tatsuno2024aisaq
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.06004'}]
tags: [Quantization, ANN Search, Has Code]
---
In approximate nearest neighbor search (ANNS) methods based on approximate
proximity graphs, DiskANN achieves good recall-speed balance for large-scale
datasets using both of RAM and storage. Despite it claims to save memory usage
by loading compressed vectors by product quantization (PQ), its memory usage
increases in proportion to the scale of datasets. In this paper, we propose
All-in-Storage ANNS with Product Quantization (AiSAQ), which offloads the
compressed vectors to storage. Our method achieves \\(\sim\\)10 MB memory usage in
query search even with billion-scale datasets with minor performance
degradation. AiSAQ also reduces the index load time before query search, which
enables the index switch between muitiple billion-scale datasets and
significantly enhances the flexibility of retrieval-augmented generation (RAG).
This method is applicable to all graph-based ANNS algorithms and can be
combined with higher-spec ANNS methods in the future.