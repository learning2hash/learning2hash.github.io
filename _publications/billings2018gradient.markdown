---
layout: publication
title: Gradient Augmented Information Retrieval With Autoencoders And Semantic Hashing
authors: Sean Billings
conference: Arxiv
year: 2018
bibkey: billings2018gradient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.04494'}]
tags: ["Evaluation", "Hashing Methods", "Text Retrieval"]
short_authors: Sean Billings
---
This paper will explore the use of autoencoders for semantic hashing in the
context of Information Retrieval. This paper will summarize how to efficiently
train an autoencoder in order to create meaningful and low-dimensional
encodings of data. This paper will demonstrate how computing and storing the
closest encodings to an input query can help speed up search time and improve
the quality of our search results. The novel contributions of this paper
involve using the representation of the data learned by an auto-encoder in
order to augment our search query in various ways. I present and evaluate the
new gradient search augmentation (GSA) approach, as well as the more well-known
pseudo-relevance-feedback (PRF) adjustment. I find that GSA helps to improve
the performance of the TF-IDF based information retrieval system, and PRF
combined with GSA works best overall for the systems compared in this paper.