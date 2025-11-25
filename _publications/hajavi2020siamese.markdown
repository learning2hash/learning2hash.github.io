---
layout: publication
title: Siamese Capsule Network For End-to-end Speaker Recognition In The Wild
authors: Amirhossein Hajavi, Ali Etemad
conference: ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2020
bibkey: hajavi2020siamese
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.13480'}]
tags: ["Evaluation", "ICASSP", "Similarity Search"]
short_authors: Amirhossein Hajavi, Ali Etemad
---
We propose an end-to-end deep model for speaker verification in the wild. Our
model uses thin-ResNet for extracting speaker embeddings from utterances and a
Siamese capsule network and dynamic routing as the Back-end to calculate a
similarity score between the embeddings. We conduct a series of experiments and
comparisons on our model to state-of-the-art solutions, showing that our model
outperforms all the other models using substantially less amount of training
data. We also perform additional experiments to study the impact of different
speaker embeddings on the Siamese capsule network. We show that the best
performance is achieved by using embeddings obtained directly from the feature
aggregation module of the Front-end and passing them to higher capsules using
dynamic routing.