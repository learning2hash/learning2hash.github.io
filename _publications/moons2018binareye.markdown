---
layout: publication
title: 'Binareye: An Always-on Energy-accuracy-scalable Binary CNN Processor With
  All Memory On Chip In 28nm CMOS'
authors: Bert Moons, Daniel Bankman, Lita Yang, Boris Murmann, Marian Verhelst
conference: 2018 IEEE Custom Integrated Circuits Conference (CICC)
year: 2018
bibkey: moons2018binareye
citations: 92
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.05554'}]
tags: ["Efficiency"]
short_authors: Moons et al.
---
This paper introduces BinarEye: a digital processor for always-on Binary
Convolutional Neural Networks. The chip maximizes data reuse through a Neuron
Array exploiting local weight Flip-Flops. It stores full network models and
feature maps and hence requires no off-chip bandwidth, which leads to a 230
1b-TOPS/W peak efficiency. Its 3 levels of flexibility - (a) weight
reconfiguration, (b) a programmable network depth and (c) a programmable
network width - allow trading energy for accuracy depending on the task's
requirements. BinarEye's full system input-to-label energy consumption ranges
from 14.4uJ/f for 86% CIFAR-10 and 98% owner recognition down to 0.92uJ/f for
94% face detection at up to 1700 frames per second. This is 3-12-70x more
efficient than the state-of-the-art at on-par accuracy.