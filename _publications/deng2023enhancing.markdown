---
layout: publication
title: Enhancing Cross-category Learning In Recommendation Systems With Multi-layer
  Embedding Training
authors: Zihao Deng, Benjamin Ghaemmaghami, Ashish Kumar Singh, Benjamin Cho, Leo
  Orshansky, Mattan Erez, Michael Orshansky
conference: Arxiv
year: 2023
bibkey: deng2023enhancing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.15881'}]
tags: ["Recommender Systems"]
short_authors: Deng et al.
---
Modern DNN-based recommendation systems rely on training-derived embeddings
of sparse features. Input sparsity makes obtaining high-quality embeddings for
rarely-occurring categories harder as their representations are updated
infrequently. We demonstrate a training-time technique to produce superior
embeddings via effective cross-category learning and theoretically explain its
surprising effectiveness. The scheme, termed the multi-layer embeddings
training (MLET), trains embeddings using factorization of the embedding layer,
with an inner dimension higher than the target embedding dimension. For
inference efficiency, MLET converts the trained two-layer embedding into a
single-layer one thus keeping inference-time model size unchanged.
  Empirical superiority of MLET is puzzling as its search space is not larger
than that of the single-layer embedding. The strong dependence of MLET on the
inner dimension is even more surprising. We develop a theory that explains both
of these behaviors by showing that MLET creates an adaptive update mechanism
modulated by the singular vectors of embeddings. When tested on multiple
state-of-the-art recommendation models for click-through rate (CTR) prediction
tasks, MLET consistently produces better models, especially for rare items. At
constant model quality, MLET allows embedding dimension, and model size,
reduction by up to 16x, and 5.8x on average, across the models.