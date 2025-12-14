---
layout: publication
title: 'Less Is More: Faster And Better Music Version Identification With Embedding
  Distillation'
authors: "Furkan Yesiler, Joan Serr\xE0, Emilia G\xF3mez"
conference: Arxiv
year: 2020
bibkey: yesiler2020less
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.03284'}]
tags: [Scalability]
short_authors: "Furkan Yesiler, Joan Serr\xE0, Emilia G\xF3mez"
---
Version identification systems aim to detect different renditions of the same
underlying musical composition (loosely called cover songs). By learning to
encode entire recordings into plain vector embeddings, recent systems have made
significant progress in bridging the gap between accuracy and scalability,
which has been a key challenge for nearly two decades. In this work, we propose
to further narrow this gap by employing a set of data distillation techniques
that reduce the embedding dimensionality of a pre-trained state-of-the-art
model. We compare a wide range of techniques and propose new ones, from
classical dimensionality reduction to more sophisticated distillation schemes.
With those, we obtain 99% smaller embeddings that, moreover, yield up to a 3%
accuracy increase. Such small embeddings can have an important impact in
retrieval time, up to the point of making a real-world system practical on a
standalone laptop.