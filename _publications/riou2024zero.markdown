---
layout: publication
title: Zero-shot Musical Stem Retrieval With Joint-embedding Predictive Architectures
authors: "Alain Riou, Antonin Gagner\xE9, Ga\xEBtan Hadjeres, Stefan Lattner, Geoffroy\
  \ Peeters"
conference: ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2025
bibkey: riou2024zero
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.19806'}]
tags: ["ICASSP"]
short_authors: Riou et al.
---
In this paper, we tackle the task of musical stem retrieval. Given a musical
mix, it consists in retrieving a stem that would fit with it, i.e., that would
sound pleasant if played together. To do so, we introduce a new method based on
Joint-Embedding Predictive Architectures, where an encoder and a predictor are
jointly trained to produce latent representations of a context and predict
latent representations of a target. In particular, we design our predictor to
be conditioned on arbitrary instruments, enabling our model to perform
zero-shot stem retrieval. In addition, we discover that pretraining the encoder
using contrastive learning drastically improves the model's performance.
  We validate the retrieval performances of our model using the MUSDB18 and
MoisesDB datasets. We show that it significantly outperforms previous baselines
on both datasets, showcasing its ability to support more or less precise (and
possibly unseen) conditioning. We also evaluate the learned embeddings on a
beat tracking task, demonstrating that they retain temporal structure and local
information.