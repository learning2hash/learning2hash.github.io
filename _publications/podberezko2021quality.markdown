---
layout: publication
title: Quality And Cost Trade-offs In Passage Re-ranking Task
authors: Pavel Podberezko, Vsevolod Mitskevich, Raman Makouski, Pavel Goncharov, Andrei
  Khobnia, Nikolay Bushkov, Marina Chernyshevich
conference: Arxiv
year: 2021
bibkey: podberezko2021quality
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.09927'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Memory Efficiency", "Re-Ranking"]
short_authors: Podberezko et al.
---
Deep learning models named transformers achieved state-of-the-art results in
a vast majority of NLP tasks at the cost of increased computational complexity
and high memory consumption. Using the transformer model in real-time inference
becomes a major challenge when implemented in production, because it requires
expensive computational resources. The more executions of a transformer are
needed the lower the overall throughput is, and switching to the smaller
encoders leads to the decrease of accuracy. Our paper is devoted to the problem
of how to choose the right architecture for the ranking step of the information
retrieval pipeline, so that the number of required calls of transformer encoder
is minimal with the maximum achievable quality of ranking. We investigated
several late-interaction models such as Colbert and Poly-encoder architectures
along with their modifications. Also, we took care of the memory footprint of
the search index and tried to apply the learning-to-hash method to binarize the
output vectors from the transformer encoders. The results of the evaluation are
provided using TREC 2019-2021 and MS Marco dev datasets.