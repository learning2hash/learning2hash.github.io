---
layout: publication
title: 'Wordrank: Learning Word Embeddings Via Robust Ranking'
authors: Shihao Ji, Hyokun Yun, Pinar Yanardag, Shin Matsushima, S. V. N. Vishwanathan
conference: Proceedings of the 2016 Conference on Empirical Methods in Natural Language
  Processing
year: 2016
bibkey: ji2015wordrank
citations: 33
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1506.02761'}]
tags: ["EMNLP", "Evaluation", "Robustness", "Tools & Libraries"]
short_authors: Ji et al.
---
Embedding words in a vector space has gained a lot of attention in recent
years. While state-of-the-art methods provide efficient computation of word
similarities via a low-dimensional matrix embedding, their motivation is often
left unclear. In this paper, we argue that word embedding can be naturally
viewed as a ranking problem due to the ranking nature of the evaluation
metrics. Then, based on this insight, we propose a novel framework WordRank
that efficiently estimates word representations via robust ranking, in which
the attention mechanism and robustness to noise are readily achieved via the
DCG-like ranking losses. The performance of WordRank is measured in word
similarity and word analogy benchmarks, and the results are compared to the
state-of-the-art word embedding techniques. Our algorithm is very competitive
to the state-of-the- arts on large corpora, while outperforms them by a
significant margin when the training set is limited (i.e., sparse and noisy).
With 17 million tokens, WordRank performs almost as well as existing methods
using 7.2 billion tokens on a popular word similarity benchmark. Our multi-node
distributed implementation of WordRank is publicly available for general usage.