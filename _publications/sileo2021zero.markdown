---
layout: publication
title: Zero-shot Recommendation As Language Modeling
authors: Damien Sileo, Wout Vossen, Robbe Raymaekers
conference: "Arxiv"
year: 2021
bibkey: sileo2021zero
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2112.04184v1"}
  - {name: "Code", url: "https://colab.research.google.com/drive/1f1mlZ-FGaLGdo5rPzxf3vemKllbh2esT?usp=sharing)"}
tags: ['ARXIV', 'Has Code', 'Supervised']
---
Recommendation is the task of ranking items (e.g. movies or products) according to individual user needs. Current systems rely on collaborative filtering and content-based techniques which both require structured training data. We propose a framework for recommendation with off-the-shelf pretrained language models (LM) that only used unstructured text corpora as training data. If a user (u) liked textitMatrix and textitInception we construct a textual prompt e.g. textitMovies like Matrix Inception (<m) to estimate the affinity between (u) and (m) with LM likelihood. We motivate our idea with a corpus analysis evaluate several prompt structures and we compare LM-based recommendation with standard matrix factorization trained on different data regimes. The code for our experiments is publicly available (https://colab.research.google.com/drive/1f1mlZ-FGaLGdo5rPzxf3vemKllbh2esT?usp=sharing).
