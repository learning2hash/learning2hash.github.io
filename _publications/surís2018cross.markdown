---
layout: publication
title: Cross-modal Embeddings For Video And Audio Retrieval
authors: "Didac Sur\xEDs, Amanda Duarte, Amaia Salvador, Jordi Torres, Xavier Gir\xF3\
  -I-Nieto"
conference: Arxiv
year: 2018
bibkey: "sur\xEDs2018cross"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.02200'}]
tags: ["Audio Retrieval", "Datasets", "Self-Supervised", "Supervised", "Video Retrieval"]
short_authors: "Sur\xEDs et al."
---
The increasing amount of online videos brings several opportunities for
training self-supervised neural networks. The creation of large scale datasets
of videos such as the YouTube-8M allows us to deal with this large amount of
data in manageable way. In this work, we find new ways of exploiting this
dataset by taking advantage of the multi-modal information it provides. By
means of a neural network, we are able to create links between audio and visual
documents, by projecting them into a common region of the feature space,
obtaining joint audio-visual embeddings. These links are used to retrieve audio
samples that fit well to a given silent video, and also to retrieve images that
match a given a query audio. The results in terms of Recall@K obtained over a
subset of YouTube-8M videos show the potential of this unsupervised approach
for cross-modal feature learning. We train embeddings for both scales and
assess their quality in a retrieval problem, formulated as using the feature
extracted from one modality to retrieve the most similar videos based on the
features computed in the other modality.