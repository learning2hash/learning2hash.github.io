---
layout: publication
title: Synthesizing Human-like Sketches From Natural Images Using A Conditional Convolutional
  Decoder
authors: "Moritz Kampelm\xFChler, Axel Pinz"
conference: 2020 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2020
bibkey: "kampelm\xFChler2020synthesizing"
citations: 17
additional_links: [{name: Code, url: 'https://github.com/kampelmuehler/synthesizing_human_like_sketches'},
  {name: Paper, url: 'https://arxiv.org/abs/2003.07101'}]
tags: []
short_authors: "Moritz Kampelm\xFChler, Axel Pinz"
---
Humans are able to precisely communicate diverse concepts by employing
sketches, a highly reduced and abstract shape based representation of visual
content. We propose, for the first time, a fully convolutional end-to-end
architecture that is able to synthesize human-like sketches of objects in
natural images with potentially cluttered background. To enable an architecture
to learn this highly abstract mapping, we employ the following key components:
(1) a fully convolutional encoder-decoder structure, (2) a perceptual
similarity loss function operating in an abstract feature space and (3)
conditioning of the decoder on the label of the object that shall be sketched.
Given the combination of these architectural concepts, we can train our
structure in an end-to-end supervised fashion on a collection of sketch-image
pairs. The generated sketches of our architecture can be classified with 85.6%
Top-5 accuracy and we verify their visual quality via a user study. We find
that deep features as a perceptual similarity metric enable image translation
with large domain gaps and our findings further show that convolutional neural
networks trained on image classification tasks implicitly learn to encode shape
information. Code is available under
https://github.com/kampelmuehler/synthesizing_human_like_sketches