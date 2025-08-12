---
layout: publication
title: 'Image Matching Across Wide Baselines: From Paper To Practice'
authors: Yuhe Jin, Dmytro Mishkin, Anastasiia Mishchuk, Jiri Matas, Pascal Fua, Kwang
  Moo Yi, Eduard Trulls
conference: International Journal of Computer Vision
year: 2020
bibkey: jin2020image
citations: 306
additional_links: [{name: Code, url: 'https://github.com/vcg-uvic/image-matching-benchmark,'},
  {name: Code, url: 'https://vision.uvic.ca/image-matching-challenge'}, {name: Paper,
    url: 'https://arxiv.org/abs/2003.01587'}]
tags: []
short_authors: Jin et al.
---
We introduce a comprehensive benchmark for local features and robust
estimation algorithms, focusing on the downstream task -- the accuracy of the
reconstructed camera pose -- as our primary metric. Our pipeline's modular
structure allows easy integration, configuration, and combination of different
methods and heuristics. This is demonstrated by embedding dozens of popular
algorithms and evaluating them, from seminal works to the cutting edge of
machine learning research. We show that with proper settings, classical
solutions may still outperform the perceived state of the art.
  Besides establishing the actual state of the art, the conducted experiments
reveal unexpected properties of Structure from Motion (SfM) pipelines that can
help improve their performance, for both algorithmic and learned methods. Data
and code are online https://github.com/vcg-uvic/image-matching-benchmark,
providing an easy-to-use and flexible framework for the benchmarking of local
features and robust estimation methods, both alongside and against
top-performing methods. This work provides a basis for the Image Matching
Challenge https://vision.uvic.ca/image-matching-challenge.