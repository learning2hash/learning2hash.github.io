---
layout: publication
title: Class-specific Variational Auto-encoder For Content-based Image Retrieval
authors: Mehdi Rafiei, Alexandros Iosifidis
conference: 2023 International Joint Conference on Neural Networks (IJCNN)
year: 2023
bibkey: rafiei2023class
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.11734'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Neural Hashing", "Supervised"]
short_authors: Mehdi Rafiei, Alexandros Iosifidis
---
Using a discriminative representation obtained by supervised deep learning
methods showed promising results on diverse Content-Based Image Retrieval
(CBIR) problems. However, existing methods exploiting labels during training
try to discriminate all available classes, which is not ideal in cases where
the retrieval problem focuses on a class of interest. In this paper, we propose
a regularized loss for Variational Auto-Encoders (VAEs) forcing the model to
focus on a given class of interest. As a result, the model learns to
discriminate the data belonging to the class of interest from any other
possibility, making the learnt latent space of the VAE suitable for
class-specific retrieval tasks. The proposed Class-Specific Variational
Auto-Encoder (CS-VAE) is evaluated on three public and one custom datasets, and
its performance is compared with that of three related VAE-based methods.
Experimental results show that the proposed method outperforms its competition
in both in-domain and out-of-domain retrieval problems.