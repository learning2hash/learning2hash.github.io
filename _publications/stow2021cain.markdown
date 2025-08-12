---
layout: publication
title: 'Cain: Automatic Code Generation For Simultaneous Convolutional Kernels On
  Focal-plane Sensor-processors'
authors: Edward Stow, Riku Murai, Sajad Saeedi, Paul H. J. Kelly
conference: Lecture Notes in Computer Science
year: 2022
bibkey: stow2021cain
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.08715'}]
tags: []
short_authors: Stow et al.
---
Focal-plane Sensor-processors (FPSPs) are a camera technology that enable low
power, high frame rate computation, making them suitable for edge computation.
Unfortunately, these devices' limited instruction sets and registers make
developing complex algorithms difficult. In this work, we present Cain - a
compiler that targets SCAMP-5, a general-purpose FPSP - which generates code
from multiple convolutional kernels. As an example, given the convolutional
kernels for an MNIST digit recognition neural network, Cain produces code that
is half as long, when compared to the other available compilers for SCAMP-5.