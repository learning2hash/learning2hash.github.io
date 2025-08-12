---
layout: publication
title: Anomaly Detection In Large Labeled Multi-graph Databases
authors: Hung T. Nguyen, Pierre J. Liang, Leman Akoglu
conference: Arxiv
year: 2020
bibkey: nguyen2020anomaly
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.03600'}]
tags: []
short_authors: Hung T. Nguyen, Pierre J. Liang, Leman Akoglu
---
Within a large database G containing graphs with labeled nodes and directed,
multi-edges; how can we detect the anomalous graphs? Most existing work are
designed for plain (unlabeled) and/or simple (unweighted) graphs. We introduce
CODETECT, the first approach that addresses the anomaly detection task for
graph databases with such complex nature. To this end, it identifies a small
representative set S of structural patterns (i.e., node-labeled network motifs)
that losslessly compress database G as concisely as possible. Graphs that do
not compress well are flagged as anomalous. CODETECT exhibits two novel
building blocks: (i) a motif-based lossless graph encoding scheme, and (ii)
fast memory-efficient search algorithms for S. We show the effectiveness of
CODETECT on transaction graph databases from three different corporations,
where existing baselines adjusted for the task fall behind significantly,
across different types of anomalies and performance metrics.