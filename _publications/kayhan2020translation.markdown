---
layout: publication
title: 'On Translation Invariance In Cnns: Convolutional Layers Can Exploit Absolute
  Spatial Location'
authors: Osman Semih Kayhan, Jan C. van Gemert
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: kayhan2020translation
citations: 164
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.07064'}]
tags: ["CVPR"]
short_authors: Osman Semih Kayhan, Jan C. van Gemert
---
In this paper we challenge the common assumption that convolutional layers in
modern CNNs are translation invariant. We show that CNNs can and will exploit
the absolute spatial location by learning filters that respond exclusively to
particular absolute locations by exploiting image boundary effects. Because
modern CNNs filters have a huge receptive field, these boundary effects operate
even far from the image boundary, allowing the network to exploit absolute
spatial location all over the image. We give a simple solution to remove
spatial location encoding which improves translation invariance and thus gives
a stronger visual inductive bias which particularly benefits small data sets.
We broadly demonstrate these benefits on several architectures and various
applications such as image classification, patch matching, and two video
classification datasets.