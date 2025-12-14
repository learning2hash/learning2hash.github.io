---
layout: publication
title: 'Matching Text And Audio Embeddings: Exploring Transfer-learning Strategies
  For Language-based Audio Retrieval'
authors: "Benno Weck, Miguel P\xE9rez Fern\xE1ndez, Holger Kirchhoff, Xavier Serra"
conference: Arxiv
year: 2022
bibkey: weck2022matching
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.02833'}]
tags: [Evaluation, Neural Hashing, Distance Metric Learning, Scalability, Tools &
    Libraries, Audio Retrieval]
short_authors: Weck et al.
---
We present an analysis of large-scale pretrained deep learning models used
for cross-modal (text-to-audio) retrieval. We use embeddings extracted by these
models in a metric learning framework to connect matching pairs of audio and
text. Shallow neural networks map the embeddings to a common dimensionality.
Our system, which is an extension of our submission to the Language-based Audio
Retrieval Task of the DCASE Challenge 2022, employs the RoBERTa foundation
model as the text embedding extractor. A pretrained PANNs model extracts the
audio embeddings. To improve the generalisation of our model, we investigate
how pretraining with audio and associated noisy text collected from the online
platform Freesound improves the performance of our method. Furthermore, our
ablation study reveals that the proper choice of the loss function and
fine-tuning the pretrained models are essential in training a competitive
retrieval system.