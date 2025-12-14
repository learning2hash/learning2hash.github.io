---
layout: publication
title: 'CANDY: A Benchmark For Continuous Approximate Nearest Neighbor Search With
  Dynamic Data Ingestion'
authors: Xianzhi Zeng, Zhuoyan Wu, Xinjing Hu, Xuanhua Shi, Shixuan Sun, Shuhao Zhang
conference: Arxiv
year: 2024
bibkey: zeng2024candy
citations: 0
additional_links: [{name: Code, url: 'https://github.com/intellistream/candy'}, {
    name: Paper, url: 'https://arxiv.org/abs/2406.19651'}]
tags: [Evaluation, Datasets, Efficiency]
short_authors: Zeng et al.
---
Approximate K Nearest Neighbor (AKNN) algorithms play a pivotal role in
various AI applications, including information retrieval, computer vision, and
natural language processing. Although numerous AKNN algorithms and benchmarks
have been developed recently to evaluate their effectiveness, the dynamic
nature of real-world data presents significant challenges that existing
benchmarks fail to address. Traditional benchmarks primarily assess retrieval
effectiveness in static contexts and often overlook update efficiency, which is
crucial for handling continuous data ingestion. This limitation results in an
incomplete assessment of an AKNN algorithms ability to adapt to changing data
patterns, thereby restricting insights into their performance in dynamic
environments. To address these gaps, we introduce CANDY, a benchmark tailored
for Continuous Approximate Nearest Neighbor Search with Dynamic Data Ingestion.
CANDY comprehensively assesses a wide range of AKNN algorithms, integrating
advanced optimizations such as machine learning-driven inference to supplant
traditional heuristic scans, and improved distance computation methods to
reduce computational overhead. Our extensive evaluations across diverse
datasets demonstrate that simpler AKNN baselines often surpass more complex
alternatives in terms of recall and latency. These findings challenge
established beliefs about the necessity of algorithmic complexity for high
performance. Furthermore, our results underscore existing challenges and
illuminate future research opportunities. We have made the datasets and
implementation methods available at: https://github.com/intellistream/candy.