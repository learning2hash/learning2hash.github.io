---
layout: publication
title: 'Binsimdb: Benchmark Dataset Construction For Fine-grained Binary Code Similarity
  Analysis'
authors: Fei Zuo et al.
conference: Arxiv
year: 2024
citations: 0
bibkey: zuo2024benchmark
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.10163'}]
tags: [Applications, Benchmarks and Datasets, Evaluation Metrics, Tools and Libraries]
---
Binary Code Similarity Analysis (BCSA) has a wide spectrum of applications,
including plagiarism detection, vulnerability discovery, and malware analysis,
thus drawing significant attention from the security community. However,
conventional techniques often face challenges in balancing both accuracy and
scalability simultaneously. To overcome these existing problems, a surge of
deep learning-based work has been recently proposed. Unfortunately, many
researchers still find it extremely difficult to conduct relevant studies or
extend existing approaches. First, prior work typically relies on proprietary
benchmark without making the entire dataset publicly accessible. Consequently,
a large-scale, well-labeled dataset for binary code similarity analysis remains
precious and scarce. Moreover, previous work has primarily focused on comparing
at the function level, rather than exploring other finer granularities.
Therefore, we argue that the lack of a fine-grained dataset for BCSA leaves a
critical gap in current research. To address these challenges, we construct a
benchmark dataset for fine-grained binary code similarity analysis called
BinSimDB, which contains equivalent pairs of smaller binary code snippets, such
as basic blocks. Specifically, we propose BMerge and BPair algorithms to bridge
the discrepancies between two binary code snippets caused by different
optimization levels or platforms. Furthermore, we empirically study the
properties of our dataset and evaluate its effectiveness for the BCSA research.
The experimental results demonstrate that BinSimDB significantly improves the
performance of binary code similarity comparison.