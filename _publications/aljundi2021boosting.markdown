---
layout: publication
title: Boosting Graph Embedding On A Single GPU
authors: "Amro Alabsi Aljundi, Taha Atahan Aky\u0131ld\u0131z, Kamer Kaya"
conference: IEEE Transactions on Parallel and Distributed Systems
year: 2021
bibkey: aljundi2021boosting
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.10049'}]
tags: ["Scalability"]
short_authors: "Amro Alabsi Aljundi, Taha Atahan Aky\u0131ld\u0131z, Kamer Kaya"
---
Graphs are ubiquitous, and they can model unique characteristics and complex
relations of real-life systems. Although using machine learning (ML) on graphs
is promising, their raw representation is not suitable for ML algorithms. Graph
embedding represents each node of a graph as a d-dimensional vector which is
more suitable for ML tasks. However, the embedding process is expensive, and
CPU-based tools do not scale to real-world graphs. In this work, we present
GOSH, a GPU-based tool for embedding large-scale graphs with minimum hardware
constraints. GOSH employs a novel graph coarsening algorithm to enhance the
impact of updates and minimize the work for embedding. It also incorporates a
decomposition schema that enables any arbitrarily large graph to be embedded
with a single GPU. As a result, GOSH sets a new state-of-the-art in link
prediction both in accuracy and speed, and delivers high-quality embeddings for
node classification at a fraction of the time compared to the state-of-the-art.
For instance, it can embed a graph with over 65 million vertices and 1.8
billion edges in less than 30 minutes on a single GPU.