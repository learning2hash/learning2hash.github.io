---
layout: publication
title: 'Reasoning Through Memorization: Nearest Neighbor Knowledge Graph Embeddings'
authors: Peng Wang, Xin Xie, Xiaohan Wang, Ningyu Zhang
conference: Lecture Notes in Computer Science
year: 2023
bibkey: wang2022reasoning
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.05575'}]
tags: ["Evaluation"]
short_authors: Wang et al.
---
Previous knowledge graph embedding approaches usually map entities to
representations and utilize score functions to predict the target entities, yet
they typically struggle to reason rare or emerging unseen entities. In this
paper, we propose kNN-KGE, a new knowledge graph embedding approach with
pre-trained language models, by linearly interpolating its entity distribution
with k-nearest neighbors. We compute the nearest neighbors based on the
distance in the entity embedding space from the knowledge store. Our approach
can allow rare or emerging entities to be memorized explicitly rather than
implicitly in model parameters. Experimental results demonstrate that our
approach can improve inductive and transductive link prediction results and
yield better performance for low-resource settings with only a few triples,
which might be easier to reason via explicit memory. Code is available at
https://github.com/zjunlp/KNN-KG.