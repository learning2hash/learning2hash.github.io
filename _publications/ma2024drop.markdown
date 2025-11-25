---
layout: publication
title: 'Drop Your Decoder: Pre-training With Bag-of-word Prediction For Dense Passage
  Retrieval'
authors: Guangyuan Ma, Xing Wu, Zijia Lin, Songlin Hu
conference: Proceedings of the 47th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2024
bibkey: ma2024drop
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.11248'}]
tags: ["SIGIR", "Unsupervised"]
short_authors: Ma et al.
---
Masked auto-encoder pre-training has emerged as a prevalent technique for
initializing and enhancing dense retrieval systems. It generally utilizes
additional Transformer decoder blocks to provide sustainable supervision
signals and compress contextual information into dense representations.
However, the underlying reasons for the effectiveness of such a pre-training
technique remain unclear. The usage of additional Transformer-based decoders
also incurs significant computational costs. In this study, we aim to shed
light on this issue by revealing that masked auto-encoder (MAE) pre-training
with enhanced decoding significantly improves the term coverage of input tokens
in dense representations, compared to vanilla BERT checkpoints. Building upon
this observation, we propose a modification to the traditional MAE by replacing
the decoder of a masked auto-encoder with a completely simplified Bag-of-Word
prediction task. This modification enables the efficient compression of lexical
signals into dense representations through unsupervised pre-training.
Remarkably, our proposed method achieves state-of-the-art retrieval performance
on several large-scale retrieval benchmarks without requiring any additional
parameters, which provides a 67% training speed-up compared to standard masked
auto-encoder pre-training with enhanced decoding.