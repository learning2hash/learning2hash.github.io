---
layout: publication
title: A Self-supervised Descriptor For Image Copy Detection
authors: Ed Pizzi, Sreya Dutta Roy, Sugosh Nagavara Ravindra, Priya Goyal, Matthijs
  Douze
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: pizzi2022self
citations: 42
additional_links: [{name: Code, url: 'https://github.com/facebookresearch/sscd-copy-detection'},
  {name: Paper, url: 'https://arxiv.org/abs/2202.10261'}]
tags: ["CVPR", "Self-Supervised"]
short_authors: Pizzi et al.
---
Image copy detection is an important task for content moderation. We
introduce SSCD, a model that builds on a recent self-supervised contrastive
training objective. We adapt this method to the copy detection task by changing
the architecture and training objective, including a pooling operator from the
instance matching literature, and adapting contrastive learning to
augmentations that combine images.
  Our approach relies on an entropy regularization term, promoting consistent
separation between descriptor vectors, and we demonstrate that this
significantly improves copy detection accuracy. Our method produces a compact
descriptor vector, suitable for real-world web scale applications. Statistical
information from a background image distribution can be incorporated into the
descriptor.
  On the recent DISC2021 benchmark, SSCD is shown to outperform both baseline
copy detection models and self-supervised architectures designed for image
classification by huge margins, in all settings. For example, SSCD out-performs
SimCLR descriptors by 48% absolute. Code is available at
https://github.com/facebookresearch/sscd-copy-detection.