---
layout: publication
title: Fast Geometric Learning With Symbolic Matrices
authors: "Jean Feydy, Alexis Glaun\xE8s, Benjamin Charlier, Michael Bronstein"
conference: Neural Information Processing Systems
year: 2020
citations: 13
bibkey: feydy2020fast
additional_links: [{name: Paper, url: 'https://papers.nips.cc/paper/2020/hash/a6292668b36ef412fa3c4102d1311a62-Abstract.html'}]
tags: [Deep Learning, NEURIPS, Theory]
---
Geometric methods rely on tensors that can be encoded using a symbolic formula and data arrays, such as kernel and distance matrices. We present an extension for standard machine learning frameworks that provides comprehensive support for this abstraction on CPUs and GPUs: our toolbox combines a versatile, transparent user interface with fast runtimes and low memory usage. Unlike general purpose acceleration frameworks such as XLA, our library turns generic Python code into binaries whose performances are competitive with state-of-the-art geometric libraries - such as FAISS for nearest neighbor search - with the added benefit of flexibility. We perform an extensive evaluation on a broad class of problems: Gaussian modelling, K-nearest neighbors search, geometric deep learning, non-Euclidean embeddings and optimal transport theory. In practice, for geometric problems that involve 1k to 1M samples in dimension 1 to 100, our library speeds up baseline GPU implementations by up to two orders of magnitude.