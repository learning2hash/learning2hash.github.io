---
layout: publication
title: 'Swindocsegmenter: An End-to-end Unified Domain Adaptive Transformer For Document
  Instance Segmentation'
authors: "Ayan Banerjee, Sanket Biswas, Josep Llad\xF3s, Umapada Pal"
conference: Lecture Notes in Computer Science
year: 2023
bibkey: banerjee2023swindocsegmenter
citations: 14
additional_links: [{name: Code, url: 'https://github.com/ayanban011/SwinDocSegmenter\}\{github.com/ayanban011/SwinDocSegmenter\'},
  {name: Paper, url: 'https://arxiv.org/abs/2305.04609'}]
tags: ["Evaluation"]
short_authors: Banerjee et al.
---
Instance-level segmentation of documents consists in assigning a class-aware
and instance-aware label to each pixel of the image. It is a key step in
document parsing for their understanding. In this paper, we present a unified
transformer encoder-decoder architecture for en-to-end instance segmentation of
complex layouts in document images. The method adapts a contrastive training
with a mixed query selection for anchor initialization in the decoder. Later
on, it performs a dot product between the obtained query embeddings and the
pixel embedding map (coming from the encoder) for semantic reasoning. Extensive
experimentation on competitive benchmarks like PubLayNet, PRIMA, Historical
Japanese (HJ), and TableBank demonstrate that our model with SwinL backbone
achieves better segmentation performance than the existing state-of-the-art
approaches with the average precision of \textbf\{93.72\}, \textbf\{54.39\},
\textbf\{84.65\} and \textbf\{98.04\} respectively under one billion parameters.
The code is made publicly available at:
\href\{https://github.com/ayanban011/SwinDocSegmenter\}\{github.com/ayanban011/SwinDocSegmenter\}