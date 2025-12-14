---
layout: publication
title: 'Fantastic Embeddings And How To Align Them: Zero-shot Inference In A Multi-shop
  Scenario'
authors: Federico Bianchi, Jacopo Tagliabue, Bingqing Yu, Luca Bigon, Ciro Greco
conference: Arxiv
year: 2020
bibkey: bianchi2020fantastic
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.14906'}]
tags: [Evaluation, Supervised, Few-shot & Zero-shot, Datasets, Unsupervised]
short_authors: Bianchi et al.
---
This paper addresses the challenge of leveraging multiple embedding spaces
for multi-shop personalization, proving that zero-shot inference is possible by
transferring shopping intent from one website to another without manual
intervention. We detail a machine learning pipeline to train and optimize
embeddings within shops first, and support the quantitative findings with
additional qualitative insights. We then turn to the harder task of using
learned embeddings across shops: if products from different shops live in the
same vector space, user intent - as represented by regions in this space - can
then be transferred in a zero-shot fashion across websites. We propose and
benchmark unsupervised and supervised methods to "travel" between embedding
spaces, each with its own assumptions on data quantity and quality. We show
that zero-shot personalization is indeed possible at scale by testing the
shared embedding space with two downstream tasks, event prediction and
type-ahead suggestions. Finally, we curate a cross-shop anonymized embeddings
dataset to foster an inclusive discussion of this important business scenario.