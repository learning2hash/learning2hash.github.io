---
layout: publication
title: Computationally Efficient NER Taggers With Combined Embeddings And Constrained
  Decoding
authors: Brian Lester, Daniel Pressel, Amy Hemmeter, Sagnik Ray Choudhury
conference: Arxiv
year: 2020
bibkey: lester2020computationally
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.01167'}]
tags: []
short_authors: Lester et al.
---
Current State-of-the-Art models in Named Entity Recognition (NER) are neural
models with a Conditional Random Field (CRF) as the final network layer, and
pre-trained "contextual embeddings". The CRF layer is used to facilitate global
coherence between labels, and the contextual embeddings provide a better
representation of words in context. However, both of these improvements come at
a high computational cost. In this work, we explore two simple techniques that
substantially improve NER performance over a strong baseline with negligible
cost. First, we use multiple pre-trained embeddings as word representations via
concatenation. Second, we constrain the tagger, trained using a cross-entropy
loss, during decoding to eliminate illegal transitions. While training a tagger
on CoNLL 2003 we find a \(786\)% speed-up over a contextual embeddings-based
tagger without sacrificing strong performance. We also show that the
concatenation technique works across multiple tasks and datasets. We analyze
aspects of similarity and coverage between pre-trained embeddings and the
dynamics of tag co-occurrence to explain why these techniques work. We provide
an open source implementation of our tagger using these techniques in three
popular deep learning frameworks --- TensorFlow, Pytorch, and DyNet.