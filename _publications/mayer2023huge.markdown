---
layout: publication
title: 'HUGE: Huge Unsupervised Graph Embeddings With Tpus'
authors: Brandon Mayer, Anton Tsitsulin, Hendrik Fichtenberger, Jonathan Halcrow,
  Bryan Perozzi
conference: Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and
  Data Mining
year: 2023
bibkey: mayer2023huge
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.14490'}]
tags: ["KDD", "Scalability", "Unsupervised"]
short_authors: Mayer et al.
---
Graphs are a representation of structured data that captures the
relationships between sets of objects. With the ubiquity of available network
data, there is increasing industrial and academic need to quickly analyze
graphs with billions of nodes and trillions of edges. A common first step for
network understanding is Graph Embedding, the process of creating a continuous
representation of nodes in a graph. A continuous representation is often more
amenable, especially at scale, for solving downstream machine learning tasks
such as classification, link prediction, and clustering. A high-performance
graph embedding architecture leveraging Tensor Processing Units (TPUs) with
configurable amounts of high-bandwidth memory is presented that simplifies the
graph embedding problem and can scale to graphs with billions of nodes and
trillions of edges. We verify the embedding space quality on real and synthetic
large-scale datasets.