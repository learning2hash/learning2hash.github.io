---
layout: publication
title: Simultaneously Learning Robust Audio Embeddings And Balanced Hash Codes For
  Query-by-example
authors: Anup Singh, Kris Demuynck, Vipul Arora
conference: ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2023
bibkey: singh2022simultaneously
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.11060'}]
tags: ["Hashing Methods", "ICASSP"]
short_authors: Anup Singh, Kris Demuynck, Vipul Arora
---
Audio fingerprinting systems must efficiently and robustly identify query
snippets in an extensive database. To this end, state-of-the-art systems use
deep learning to generate compact audio fingerprints. These systems deploy
indexing methods, which quantize fingerprints to hash codes in an unsupervised
manner to expedite the search. However, these methods generate imbalanced hash
codes, leading to their suboptimal performance. Therefore, we propose a
self-supervised learning framework to compute fingerprints and balanced hash
codes in an end-to-end manner to achieve both fast and accurate retrieval
performance. We model hash codes as a balanced clustering process, which we
regard as an instance of the optimal transport problem. Experimental results
indicate that the proposed approach improves retrieval efficiency while
preserving high accuracy, particularly at high distortion levels, compared to
the competing methods. Moreover, our system is efficient and scalable in
computational load and memory storage.