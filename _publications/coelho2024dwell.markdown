---
layout: publication
title: 'Dwell In The Beginning: How Language Models Embed Long Documents For Dense
  Retrieval'
authors: "Jo\xE3o Coelho, Bruno Martins, Jo\xE3o Magalh\xE3es, Jamie Callan, Chenyan\
  \ Xiong"
conference: 'Proceedings of the 62nd Annual Meeting of the Association for Computational
  Linguistics (Volume 2: Short Papers)'
year: 2024
bibkey: coelho2024dwell
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.04163'}]
tags: [Text Retrieval, ACL]
short_authors: Coelho et al.
---
This study investigates the existence of positional biases in
Transformer-based models for text representation learning, particularly in the
context of web document retrieval. We build on previous research that
demonstrated loss of information in the middle of input sequences for causal
language models, extending it to the domain of representation learning. We
examine positional biases at various stages of training for an encoder-decoder
model, including language model pre-training, contrastive pre-training, and
contrastive fine-tuning. Experiments with the MS-MARCO document collection
reveal that after contrastive pre-training the model already generates
embeddings that better capture early contents of the input, with fine-tuning
further aggravating this effect.