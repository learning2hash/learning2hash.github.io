---
layout: publication
title: 'Figuring Out Figures: Using Textual References To Caption Scientific Figures'
authors: Stanley Cao, Kevin Liu
conference: Arxiv
year: 2024
bibkey: cao2024figuring
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.11008'}]
tags: []
short_authors: Stanley Cao, Kevin Liu
---
Figures are essential channels for densely communicating complex ideas in
scientific papers. Previous work in automatically generating figure captions
has been largely unsuccessful and has defaulted to using single-layer LSTMs,
which no longer achieve state-of-the-art performance. In our work, we use the
SciCap datasets curated by Hsu et al. and use a variant of a CLIP+GPT-2
encoder-decoder model with cross-attention to generate captions conditioned on
the image. Furthermore, we augment our training pipeline by creating a new
dataset MetaSciCap that incorporates textual metadata from the original paper
relevant to the figure, such as the title, abstract, and in-text references. We
use SciBERT to encode the textual metadata and use this encoding alongside the
figure embedding. In our experimentation with different models, we found that
the CLIP+GPT-2 model performs better when it receives all textual metadata from
the SciBERT encoder in addition to the figure, but employing a SciBERT+GPT2
model that uses only the textual metadata achieved optimal performance.