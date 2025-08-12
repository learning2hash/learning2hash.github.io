---
layout: publication
title: Low-shot Learning With Large-scale Diffusion
authors: "Matthijs Douze, Arthur Szlam, Bharath Hariharan, Herv\xE9 J\xE9gou"
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: douze2017low
citations: 124
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.02332'}]
tags: ["CVPR"]
short_authors: Douze et al.
---
This paper considers the problem of inferring image labels from images when
only a few annotated examples are available at training time. This setup is
often referred to as low-shot learning, where a standard approach is to
re-train the last few layers of a convolutional neural network learned on
separate classes for which training examples are abundant. We consider a
semi-supervised setting based on a large collection of images to support label
propagation. This is possible by leveraging the recent advances on large-scale
similarity graph construction.
  We show that despite its conceptual simplicity, scaling label propagation up
to hundred millions of images leads to state of the art accuracy in the
low-shot learning regime.