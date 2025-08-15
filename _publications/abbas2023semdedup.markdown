---
layout: publication
title: 'Semdedup: Data-efficient Learning At Web-scale Through Semantic Deduplication'
authors: "Amro Abbas, Kushal Tirumala, D\xE1niel Simig, Surya Ganguli, Ari S. Morcos"
conference: Arxiv
year: 2023
bibkey: abbas2023semdedup
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.09540'}]
tags: ["Datasets", "Efficiency", "Evaluation"]
short_authors: Abbas et al.
---
Progress in machine learning has been driven in large part by massive
increases in data. However, large web-scale datasets such as LAION are largely
uncurated beyond searches for exact duplicates, potentially leaving much
redundancy. Here, we introduce SemDeDup, a method which leverages embeddings
from pre-trained models to identify and remove semantic duplicates: data pairs
which are semantically similar, but not exactly identical. Removing semantic
duplicates preserves performance and speeds up learning. Analyzing a subset of
LAION, we show that SemDeDup can remove 50% of the data with minimal
performance loss, effectively halving training time. Moreover, performance
increases out of distribution. Also, analyzing language models trained on C4, a
partially curated dataset, we show that SemDeDup improves over prior approaches
while providing efficiency gains. SemDeDup provides an example of how simple
ways of leveraging quality embeddings can be used to make models learn faster
with less data.