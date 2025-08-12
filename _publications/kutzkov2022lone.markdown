---
layout: publication
title: 'Lone Sampler: Graph Node Embeddings By Coordinated Local Neighborhood Sampling'
authors: Konstantin Kutzkov
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2023
bibkey: kutzkov2022lone
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.15114'}]
tags: ["AAAI"]
short_authors: Konstantin Kutzkov
---
Local graph neighborhood sampling is a fundamental computational problem that
is at the heart of algorithms for node representation learning. Several works
have presented algorithms for learning discrete node embeddings where graph
nodes are represented by discrete features such as attributes of neighborhood
nodes. Discrete embeddings offer several advantages compared to continuous
word2vec-like node embeddings: ease of computation, scalability, and
interpretability. We present LoNe Sampler, a suite of algorithms for generating
discrete node embeddings by Local Neighborhood Sampling, and address two
shortcomings of previous work. First, our algorithms have rigorously understood
theoretical properties. Second, we show how to generate approximate explicit
vector maps that avoid the expensive computation of a Gram matrix for the
training of a kernel model. Experiments on benchmark datasets confirm the
theoretical findings and demonstrate the advantages of the proposed methods.