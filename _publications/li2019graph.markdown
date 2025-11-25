---
layout: publication
title: Graph Matching Networks For Learning The Similarity Of Graph Structured Objects
authors: Yujia Li, Chenjie Gu, Thomas Dullien, Oriol Vinyals, Pushmeet Kohli
conference: Arxiv
year: 2019
bibkey: li2019graph
citations: 234
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.12787'}]
tags: ["Graph Based ANN", "Similarity Search", "Supervised"]
short_authors: Li et al.
---
This paper addresses the challenging problem of retrieval and matching of
graph structured objects, and makes two key contributions. First, we
demonstrate how Graph Neural Networks (GNN), which have emerged as an effective
model for various supervised prediction problems defined on structured data,
can be trained to produce embedding of graphs in vector spaces that enables
efficient similarity reasoning. Second, we propose a novel Graph Matching
Network model that, given a pair of graphs as input, computes a similarity
score between them by jointly reasoning on the pair through a new cross-graph
attention-based matching mechanism. We demonstrate the effectiveness of our
models on different domains including the challenging problem of
control-flow-graph based function similarity search that plays an important
role in the detection of vulnerabilities in software systems. The experimental
analysis demonstrates that our models are not only able to exploit structure in
the context of similarity learning but they can also outperform domain-specific
baseline systems that have been carefully hand-engineered for these problems.