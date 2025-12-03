---
layout: publication
title: 'ACTGNN: Assessment Of Clustering Tendency With Synthetically-trained Graph
  Neural Networks'
authors: Yiran Luo, Evangelos E. Papalexakis
conference: Lecture Notes in Computer Science
year: 2025
bibkey: luo2025actgnn
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.18112'}]
tags: ["Datasets", "Distance Metric Learning", "Graph Based ANN", "Hashing Methods", "Locality-Sensitive-Hashing"]
short_authors: Yiran Luo, Evangelos E. Papalexakis
---
Determining clustering tendency in datasets is a fundamental but challenging
task, especially in noisy or high-dimensional settings where traditional
methods, such as the Hopkins Statistic and Visual Assessment of Tendency (VAT),
often struggle to produce reliable results. In this paper, we propose ACTGNN, a
graph-based framework designed to assess clustering tendency by leveraging
graph representations of data. Node features are constructed using
Locality-Sensitive Hashing (LSH), which captures local neighborhood
information, while edge features incorporate multiple similarity metrics, such
as the Radial Basis Function (RBF) kernel, to model pairwise relationships. A
Graph Neural Network (GNN) is trained exclusively on synthetic datasets,
enabling robust learning of clustering structures under controlled conditions.
Extensive experiments demonstrate that ACTGNN significantly outperforms
baseline methods on both synthetic and real-world datasets, exhibiting superior
performance in detecting faint clustering structures, even in high-dimensional
or noisy data. Our results highlight the generalizability and effectiveness of
the proposed approach, making it a promising tool for robust clustering
tendency assessment.