---
layout: publication
title: 'LIST: Learning To Index Spatio-textual Data For Embedding Based Spatial Keyword
  Queries'
authors: Ziqi Yin, Shanshan Feng, Shang Liu, Gao Cong, Yew Soon Ong, Bin Cui
conference: Arxiv
year: 2024
bibkey: yin2024list
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.07331'}]
tags: [Re-ranking, Similarity Search, Neural Hashing, Efficiency, Hybrid ANN Methods]
short_authors: Yin et al.
---
With the proliferation of spatio-textual data, Top-k KNN spatial keyword
queries (TkQs), which return a list of objects based on a ranking function that
considers both spatial and textual relevance, have found many real-life
applications. To efficiently handle TkQs, many indexes have been developed, but
the effectiveness of TkQ is limited. To improve effectiveness, several deep
learning models have recently been proposed, but they suffer severe efficiency
issues and there are no efficient indexes specifically designed to accelerate
the top-k search process for these deep learning models. To tackle these
issues, we consider embedding based spatial keyword queries, which capture the
semantic meaning of query keywords and object descriptions in two separate
embeddings to evaluate textual relevance. Although various models can be used
to generate these embeddings, no indexes have been specifically designed for
such queries. To fill this gap, we propose LIST, a novel machine learning based
Approximate Nearest Neighbor Search index that Learns to Index the
Spatio-Textual data. LIST utilizes a new learning-to-cluster technique to group
relevant queries and objects together while separating irrelevant queries and
objects. There are two key challenges in building an effective and efficient
index, i.e., the absence of high-quality labels and the unbalanced clustering
results. We develop a novel pseudo-label generation technique to address the
two challenges. Additionally, we introduce a learning based spatial relevance
model that can integrates with various text relevance models to form a
lightweight yet effective relevance for reranking objects retrieved by LIST.