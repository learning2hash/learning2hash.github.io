---
layout: publication
title: Learning Effective Representations For Retrieval Using Self-distillation With
  Adaptive Relevance Margins
authors: Lukas Gienapp, Niklas Deckers, Martin Potthast, Harrisen Scells
conference: Proceedings of the 2025 International ACM SIGIR Conference on Innovative
  Concepts and Theories in Information Retrieval (ICTIR)
year: 2024
bibkey: gienapp2024learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.21515'}]
tags: ["Efficiency", "SIGIR", "Self-Supervised"]
short_authors: Gienapp et al.
---
Representation-based retrieval models, so-called bi-encoders, estimate the relevance of a document to a query by calculating the similarity of their respective embeddings. Current state-of-the-art bi-encoders are trained using an expensive training regime involving knowledge distillation from a teacher model and batch-sampling. Instead of relying on a teacher model, we contribute a novel parameter-free loss function for self-supervision that exploits the pre-trained language modeling capabilities of the encoder model as a training signal, eliminating the need for batch sampling by performing implicit hard negative mining. We investigate the capabilities of our proposed approach through extensive experiments, demonstrating that self-distillation can match the effectiveness of teacher distillation using only 13.5% of the data, while offering a speedup in training time between 3x and 15x compared to parametrized losses. All code and data is made openly available.