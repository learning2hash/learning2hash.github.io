---
layout: publication
title: Hamming Sentence Embeddings for Information Retrieval
authors: Hamann Felix, Kurz Nadja, Ulges Adrian
conference: "Arxiv"
year: 2019
bibkey: hamann2019hamming
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1908.05541"}
tags: ['ARXIV', 'General']
---
In retrieval applications binary hashes are known to offer significant improvements in terms of both memory and speed. We investigate the compression of sentence embeddings using a neural encoder-decoder architecture which is trained by minimizing reconstruction error. Instead of employing the original real-valued embeddings we use latent representations in Hamming space produced by the encoder for similarity calculations. In quantitative experiments on several benchmarks for semantic similarity tasks we show that our compressed hamming embeddings yield a comparable performance to uncompressed embeddings (Sent2Vec InferSent Glove-BoW) at compression ratios of up to 2561. We further demonstrate that our model strongly decorrelates input features and that the compressor generalizes well when pre-trained on Wikipedia sentences. We publish the source code on Github and all experimental results.
