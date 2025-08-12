---
layout: publication
title: Clinical Concept Embeddings Learned From Massive Sources Of Multimodal Medical
  Data
authors: Andrew L. Beam, Benjamin Kompa, Allen Schmaltz, Inbar Fried, Griffin Weber,
  Nathan P. Palmer, Xu Shi, Tianxi Cai, Isaac S. Kohane
conference: Biocomputing 2020
year: 2019
bibkey: beam2018clinical
citations: 162
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.01486'}]
tags: ["Unsupervised"]
short_authors: Beam et al.
---
Word embeddings are a popular approach to unsupervised learning of word
relationships that are widely used in natural language processing. In this
article, we present a new set of embeddings for medical concepts learned using
an extremely large collection of multimodal medical data. Leaning on recent
theoretical insights, we demonstrate how an insurance claims database of 60
million members, a collection of 20 million clinical notes, and 1.7 million
full text biomedical journal articles can be combined to embed concepts into a
common space, resulting in the largest ever set of embeddings for 108,477
medical concepts. To evaluate our approach, we present a new benchmark
methodology based on statistical power specifically designed to test embeddings
of medical concepts. Our approach, called cui2vec, attains state-of-the-art
performance relative to previous methods in most instances. Finally, we provide
a downloadable set of pre-trained embeddings for other researchers to use, as
well as an online tool for interactive exploration of the cui2vec embeddings