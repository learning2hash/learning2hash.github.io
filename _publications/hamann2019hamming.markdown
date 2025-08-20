---
layout: publication
title: Hamming Sentence Embeddings For Information Retrieval
authors: Felix Hamann, Nadja Kurz, Adrian Ulges
conference: Arxiv
year: 2019
bibkey: hamann2019hamming
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.05541'}]
tags: [Evaluation, Hashing Methods]
short_authors: Felix Hamann, Nadja Kurz, Adrian Ulges
---
In retrieval applications, binary hashes are known to offer significant
improvements in terms of both memory and speed. We investigate the compression
of sentence embeddings using a neural encoder-decoder architecture, which is
trained by minimizing reconstruction error. Instead of employing the original
real-valued embeddings, we use latent representations in Hamming space produced
by the encoder for similarity calculations.
  In quantitative experiments on several benchmarks for semantic similarity
tasks, we show that our compressed hamming embeddings yield a comparable
performance to uncompressed embeddings (Sent2Vec, InferSent, Glove-BoW), at
compression ratios of up to 256:1. We further demonstrate that our model
strongly decorrelates input features, and that the compressor generalizes well
when pre-trained on Wikipedia sentences. We publish the source code on Github
and all experimental results.