---
layout: publication
title: 'Aisaq: All-in-storage ANNS With Product Quantization For Dram-free Information
  Retrieval'
authors: Kento Tatsuno, Daisuke Miyashita, Taiga Ikeda, Kiyoshi Ishiyama, Kazunari
  Sumiyoshi, Jun Deguchi
conference: Arxiv
year: 2024
bibkey: tatsuno2024aisaq
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.06004'}]
tags: ["Graph Based ANN", "Large Scale Search", "Memory Efficiency", "Quantization", "Scalability"]
short_authors: Tatsuno et al.
---
Graph-based approximate nearest neighbor search (ANNS) algorithms work
effectively against large-scale vector retrieval. Among such methods, DiskANN
achieves good recall-speed tradeoffs using both DRAM and storage. DiskANN
adopts product quantization (PQ) to reduce memory usage, which is still
proportional to the scale of datasets. In this paper, we propose All-in-Storage
ANNS with Product Quantization (AiSAQ), which offloads compressed vectors to
the SSD index. Our method achieves \(\sim\)10 MB memory usage in query search
with billion-scale datasets without critical latency degradation. AiSAQ also
reduces the index load time for query search preparation, which enables fast
switch between muitiple billion-scale indices.This method can be applied to
retrievers of retrieval-augmented generation (RAG) and be scaled out with
multiple-server systems for emerging datasets. Our DiskANN-based implementation
is available on GitHub.