---
layout: publication
title: 'Distributed Convolutional Dictionary Learning (dicodile): Pattern Discovery
  In Large Images And Signals'
authors: Thomas Moreau, Alexandre Gramfort
conference: Arxiv
year: 2019
bibkey: moreau2019distributed
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.09235'}]
tags: []
short_authors: Thomas Moreau, Alexandre Gramfort
---
Convolutional dictionary learning (CDL) estimates shift invariant basis
adapted to multidimensional data. CDL has proven useful for image denoising or
inpainting, as well as for pattern discovery on multivariate signals. As
estimated patterns can be positioned anywhere in signals or images,
optimization techniques face the difficulty of working in extremely high
dimensions with millions of pixels or time samples, contrarily to standard
patch-based dictionary learning. To address this optimization problem, this
work proposes a distributed and asynchronous algorithm, employing locally
greedy coordinate descent and an asynchronous locking mechanism that does not
require a central server. This algorithm can be used to distribute the
computation on a number of workers which scales linearly with the encoded
signal's size. Experiments confirm the scaling properties which allows us to
learn patterns on large scales images from the Hubble Space Telescope.