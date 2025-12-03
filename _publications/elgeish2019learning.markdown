---
layout: publication
title: Learning Joint Acoustic-phonetic Word Embeddings
authors: Mohamed El-Geish
conference: Arxiv
year: 2019
bibkey: elgeish2019learning
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.00493'}]
tags: ["Distance Metric Learning", "Evaluation", "Neural Hashing", "Supervised"]
short_authors: Mohamed El-Geish
---
Most speech recognition tasks pertain to mapping words across two modalities:
acoustic and orthographic. In this work, we suggest learning encoders that map
variable-length, acoustic or phonetic, sequences that represent words into
fixed-dimensional vectors in a shared latent space; such that the distance
between two word vectors represents how closely the two words sound. Instead of
directly learning the distances between word vectors, we employ weak
supervision and model a binary classification task to predict whether two
inputs, one of each modality, represent the same word given a distance
threshold. We explore various deep-learning models, bimodal contrastive losses,
and techniques for mining hard negative examples such as the semi-supervised
technique of self-labeling. Our best model achieves an \(F_1\) score of 0.95 for
the binary classification task.