---
layout: publication
title: Detecting Kissing Scenes In A Database Of Hollywood Films
authors: Amir Ziai
conference: Arxiv
year: 2019
bibkey: ziai2019detecting
citations: 2
additional_links: [{name: Code, url: 'http://github.com/amirziai/kissing-detector'},
  {name: Paper, url: 'https://arxiv.org/abs/1906.01843'}]
tags: ["Datasets", "Video Retrieval"]
short_authors: Amir Ziai
---
Detecting scene types in a movie can be very useful for application such as
video editing, ratings assignment, and personalization. We propose a system for
detecting kissing scenes in a movie. This system consists of two components.
The first component is a binary classifier that predicts a binary label (i.e.
kissing or not) given a features exctracted from both the still frames and
audio waves of a one-second segment. The second component aggregates the binary
labels for contiguous non-overlapping segments into a set of kissing scenes. We
experimented with a variety of 2D and 3D convolutional architectures such as
ResNet, DesnseNet, and VGGish and developed a highly accurate kissing detector
that achieves a validation F1 score of 0.95 on a diverse database of Hollywood
films ranging many genres and spanning multiple decades. The code for this
project is available at http://github.com/amirziai/kissing-detector.