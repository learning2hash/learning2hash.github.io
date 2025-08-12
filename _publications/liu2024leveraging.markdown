---
layout: publication
title: Leveraging LLM Embeddings For Cross Dataset Label Alignment And Zero Shot Music
  Emotion Prediction
authors: Renhang Liu, Abhinaba Roy, Dorien Herremans
conference: Arxiv
year: 2024
bibkey: liu2024leveraging
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.11522'}]
tags: ["Datasets", "Few Shot & Zero Shot"]
short_authors: Renhang Liu, Abhinaba Roy, Dorien Herremans
---
In this work, we present a novel method for music emotion recognition that
leverages Large Language Model (LLM) embeddings for label alignment across
multiple datasets and zero-shot prediction on novel categories. First, we
compute LLM embeddings for emotion labels and apply non-parametric clustering
to group similar labels, across multiple datasets containing disjoint labels.
We use these cluster centers to map music features (MERT) to the LLM embedding
space. To further enhance the model, we introduce an alignment regularization
that enables dissociation of MERT embeddings from different clusters. This
further enhances the model's ability to better adaptation to unseen datasets.
We demonstrate the effectiveness of our approach by performing zero-shot
inference on a new dataset, showcasing its ability to generalize to unseen
labels without additional training.