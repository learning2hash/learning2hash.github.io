---
layout: publication
title: Associative Embedding For Game-agnostic Team Discrimination
authors: Maxime Istasse, Julien Moreau, Christophe de Vleeschouwer
conference: The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
  Workshops 2019
year: 2019
bibkey: istasse2019associative
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.01058'}]
tags: ["CVPR"]
short_authors: Maxime Istasse, Julien Moreau, Christophe de Vleeschouwer
---
Assigning team labels to players in a sport game is not a trivial task when
no prior is known about the visual appearance of each team. Our work builds on
a Convolutional Neural Network (CNN) to learn a descriptor, namely a pixel-wise
embedding vector, that is similar for pixels depicting players from the same
team, and dissimilar when pixels correspond to distinct teams. The advantage of
this idea is that no per-game learning is needed, allowing efficient team
discrimination as soon as the game starts. In principle, the approach follows
the associative embedding framework introduced in arXiv:1611.05424 to
differentiate instances of objects. Our work is however different in that it
derives the embeddings from a lightweight segmentation network and, more
fundamentally, because it considers the assignment of the same embedding to
unconnected pixels, as required by pixels of distinct players from the same
team. Excellent results, both in terms of team labelling accuracy and
generalization to new games/arenas, have been achieved on panoramic views of a
large variety of basketball games involving players interactions and
occlusions. This makes our method a good candidate to integrate team separation
in many CNN-based sport analytics pipelines.