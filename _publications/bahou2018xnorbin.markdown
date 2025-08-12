---
layout: publication
title: 'XNORBIN: A 95 Top/s/w Hardware Accelerator For Binary Convolutional Neural
  Networks'
authors: Andrawes Al Bahou, Geethan Karunaratne, Renzo Andri, Lukas Cavigelli, Luca
  Benini
conference: 2018 IEEE Symposium in Low-Power and High-Speed Chips (COOL CHIPS)
year: 2018
bibkey: bahou2018xnorbin
citations: 46
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.05849'}]
tags: ["Efficiency", "Quantization"]
short_authors: Bahou et al.
---
Deploying state-of-the-art CNNs requires power-hungry processors and off-chip
memory. This precludes the implementation of CNNs in low-power embedded
systems. Recent research shows CNNs sustain extreme quantization, binarizing
their weights and intermediate feature maps, thereby saving 8-32\x memory and
collapsing energy-intensive sum-of-products into XNOR-and-popcount operations.
  We present XNORBIN, an accelerator for binary CNNs with computation tightly
coupled to memory for aggressive data reuse. Implemented in UMC 65nm technology
XNORBIN achieves an energy efficiency of 95 TOp/s/W and an area efficiency of
2.0 TOp/s/MGE at 0.8 V.