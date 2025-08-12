---
layout: publication
title: Learning Sequential Descriptors For Sequence-based Visual Place Recognition
authors: Riccardo Mereu, Gabriele Trivigno, Gabriele Berton, Carlo Masone, Barbara
  Caputo
conference: IEEE Robotics and Automation Letters
year: 2022
bibkey: mereu2022learning
citations: 21
additional_links: [{name: Code, url: 'https://github.com/vandal-vpr/vg-transformers'},
  {name: Paper, url: 'https://arxiv.org/abs/2207.03868'}]
tags: []
short_authors: Mereu et al.
---
In robotics, Visual Place Recognition is a continuous process that receives
as input a video stream to produce a hypothesis of the robot's current position
within a map of known places. This task requires robust, scalable, and
efficient techniques for real applications. This work proposes a detailed
taxonomy of techniques using sequential descriptors, highlighting different
mechanism to fuse the information from the individual images. This
categorization is supported by a complete benchmark of experimental results
that provides evidence on the strengths and weaknesses of these different
architectural choices. In comparison to existing sequential descriptors
methods, we further investigate the viability of Transformers instead of CNN
backbones, and we propose a new ad-hoc sequence-level aggregator called
SeqVLAD, which outperforms prior state of the art on different datasets. The
code is available at https://github.com/vandal-vpr/vg-transformers.