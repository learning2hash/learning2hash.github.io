---
layout: publication
title: End-to-end Retrieval With Learned Dense And Sparse Representations Using Lucene
authors: Haonan Chen, Carlos Lassance, Jimmy Lin
conference: Arxiv
year: 2023
bibkey: chen2023end
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.18503'}]
tags: ["Graph Based ANN", "Similarity Search", "Tools & Libraries"]
short_authors: Haonan Chen, Carlos Lassance, Jimmy Lin
---
The bi-encoder architecture provides a framework for understanding
machine-learned retrieval models based on dense and sparse vector
representations. Although these representations capture parametric realizations
of the same underlying conceptual framework, their respective implementations
of top-\(k\) similarity search require the coordination of different software
components (e.g., inverted indexes, HNSW indexes, and toolkits for neural
inference), often knitted together in complex architectures. In this work, we
ask the following question: What's the simplest design, in terms of requiring
the fewest changes to existing infrastructure, that can support end-to-end
retrieval with modern dense and sparse representations? The answer appears to
be that Lucene is sufficient, as we demonstrate in Anserini, a toolkit for
reproducible information retrieval research. That is, effective retrieval with
modern single-vector neural models can be efficiently performed directly in
Java on the CPU. We examine the implications of this design for information
retrieval researchers pushing the state of the art as well as for software
engineers building production search systems.