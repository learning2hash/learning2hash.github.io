---
layout: publication
title: Self-supervised Contrastive Learning For Robust Audio-sheet Music Retrieval
  Systems
authors: "Carvalho Luis, Wash\xFCttl Tobias, Widmer Gerhard"
conference: Proceedings of the 14th ACM Multimedia Systems Conference
year: 2023
bibkey: carvalho2023self
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.12134'}]
tags: ["Audio Retrieval", "Evaluation", "Robustness", "Self-Supervised"]
short_authors: "Carvalho Luis, Wash\xFCttl Tobias, Widmer Gerhard"
---
Linking sheet music images to audio recordings remains a key problem for the
development of efficient cross-modal music retrieval systems. One of the
fundamental approaches toward this task is to learn a cross-modal embedding
space via deep neural networks that is able to connect short snippets of audio
and sheet music. However, the scarcity of annotated data from real musical
content affects the capability of such methods to generalize to real retrieval
scenarios. In this work, we investigate whether we can mitigate this limitation
with self-supervised contrastive learning, by exposing a network to a large
amount of real music data as a pre-training step, by contrasting randomly
augmented views of snippets of both modalities, namely audio and sheet images.
Through a number of experiments on synthetic and real piano data, we show that
pre-trained models are able to retrieve snippets with better precision in all
scenarios and pre-training configurations. Encouraged by these results, we
employ the snippet embeddings in the higher-level task of cross-modal piece
identification and conduct more experiments on several retrieval
configurations. In this task, we observe that the retrieval quality improves
from 30% up to 100% when real music data is present. We then conclude by
arguing for the potential of self-supervised contrastive learning for
alleviating the annotated data scarcity in multi-modal music retrieval models.