---
layout: publication
title: A Simple Interpretable Transformer For Fine-grained Image Classification And
  Analysis
authors: Dipanjyoti Paul, Arpita Chowdhury, Xinqi Xiong, Feng-Ju Chang, David Carlyn,
  Samuel Stevens, Kaiya L. Provost, Anuj Karpatne, Bryan Carstens, Daniel Rubenstein,
  Charles Stewart, Tanya Berger-Wolf, Yu Su, Wei-Lun Chao
conference: Arxiv
year: 2023
bibkey: paul2023simple
citations: 2
additional_links: [{name: Code, url: 'https://github.com/Imageomics/INTR'}, {name: Paper,
    url: 'https://arxiv.org/abs/2311.04157'}]
tags: []
short_authors: Paul et al.
---
We present a novel usage of Transformers to make image classification
interpretable. Unlike mainstream classifiers that wait until the last fully
connected layer to incorporate class information to make predictions, we
investigate a proactive approach, asking each class to search for itself in an
image. We realize this idea via a Transformer encoder-decoder inspired by
DEtection TRansformer (DETR). We learn "class-specific" queries (one for each
class) as input to the decoder, enabling each class to localize its patterns in
an image via cross-attention. We name our approach INterpretable TRansformer
(INTR), which is fairly easy to implement and exhibits several compelling
properties. We show that INTR intrinsically encourages each class to attend
distinctively; the cross-attention weights thus provide a faithful
interpretation of the prediction. Interestingly, via "multi-head"
cross-attention, INTR could identify different "attributes" of a class, making
it particularly suitable for fine-grained classification and analysis, which we
demonstrate on eight datasets. Our code and pre-trained models are publicly
accessible at the Imageomics Institute GitHub site:
https://github.com/Imageomics/INTR.