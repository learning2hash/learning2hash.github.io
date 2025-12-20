---
layout: publication
title: 'KATE: K-competitive Autoencoder For Text'
authors: Yu Chen, Mohammed J. Zaki
conference: Arxiv
year: 2017
bibkey: chen2017kate
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.02033'}]
tags: ["Datasets", "Evaluation"]
short_authors: Yu Chen, Mohammed J. Zaki
---
Autoencoders have been successful in learning meaningful representations from
image datasets. However, their performance on text datasets has not been widely
studied. Traditional autoencoders tend to learn possibly trivial
representations of text documents due to their confounding properties such as
high-dimensionality, sparsity and power-law word distributions. In this paper,
we propose a novel k-competitive autoencoder, called KATE, for text documents.
Due to the competition between the neurons in the hidden layer, each neuron
becomes specialized in recognizing specific data patterns, and overall the
model can learn meaningful representations of textual data. A comprehensive set
of experiments show that KATE can learn better representations than traditional
autoencoders including denoising, contractive, variational, and k-sparse
autoencoders. Our model also outperforms deep generative models, probabilistic
topic models, and even word representation models (e.g., Word2Vec) in terms of
several downstream tasks such as document classification, regression, and
retrieval.