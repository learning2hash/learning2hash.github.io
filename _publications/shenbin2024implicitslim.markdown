---
layout: publication
title: Implicitslim And How It Improves Embedding-based Collaborative Filtering
authors: Ilya Shenbin, Sergey Nikolenko
conference: Arxiv
year: 2024
bibkey: shenbin2024implicitslim
citations: 0
additional_links: [{name: Code, url: 'https://github.com/ilya-shenbin/ImplicitSLIM'},
  {name: Paper, url: 'https://arxiv.org/abs/2406.00198'}]
tags: ["Evaluation", "Recommender Systems", "Supervised", "Unsupervised"]
short_authors: Ilya Shenbin, Sergey Nikolenko
---
We present ImplicitSLIM, a novel unsupervised learning approach for sparse
high-dimensional data, with applications to collaborative filtering. Sparse
linear methods (SLIM) and their variations show outstanding performance, but
they are memory-intensive and hard to scale. ImplicitSLIM improves
embedding-based models by extracting embeddings from SLIM-like models in a
computationally cheap and memory-efficient way, without explicit learning of
heavy SLIM-like models. We show that ImplicitSLIM improves performance and
speeds up convergence for both state of the art and classical collaborative
filtering methods. The source code for ImplicitSLIM, related models, and
applications is available at https://github.com/ilya-shenbin/ImplicitSLIM.