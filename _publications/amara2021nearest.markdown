---
layout: publication
title: 'Nearest Neighbor Search With Compact Codes: A Decoder Perspective'
authors: Kenza Amara, Matthijs Douze, Alexandre Sablayrolles, Hervé Jégou
conference: "Arxiv"
year: 2021
citations: 1
bibkey: amara2021nearest
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2112.09568'}
tags: ['Cross-Modal', 'Model Design', 'Quantisation', 'Retrieval Models', 'Shallow', 'Datasets', 'Quantization', 'Hashing']
---
Modern approaches for fast retrieval of similar vectors on billion-scaled
datasets rely on compressed-domain approaches such as binary sketches or
product quantization. These methods minimize a certain loss, typically the mean
squared error or other objective functions tailored to the retrieval problem.
In this paper, we re-interpret popular methods such as binary hashing or
product quantizers as auto-encoders, and point out that they implicitly make
suboptimal assumptions on the form of the decoder. We design
backward-compatible decoders that improve the reconstruction of the vectors
from the same codes, which translates to a better performance in nearest
neighbor search. Our method significantly improves over binary hashing methods
or product quantization on popular benchmarks.
