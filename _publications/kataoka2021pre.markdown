---
layout: publication
title: Pre-training Without Natural Images
authors: Hirokatsu Kataoka, Kazushige Okayasu, Asato Matsumoto, Eisuke Yamagata, Ryosuke
  Yamada, Nakamasa Inoue, Akio Nakamura, Yutaka Satoh
conference: Lecture Notes in Computer Science
year: 2021
bibkey: kataoka2021pre
citations: 51
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.08515'}]
tags: []
short_authors: Kataoka et al.
---
Is it possible to use convolutional neural networks pre-trained without any
natural images to assist natural image understanding? The paper proposes a
novel concept, Formula-driven Supervised Learning. We automatically generate
image patterns and their category labels by assigning fractals, which are based
on a natural law existing in the background knowledge of the real world.
Theoretically, the use of automatically generated images instead of natural
images in the pre-training phase allows us to generate an infinite scale
dataset of labeled images. Although the models pre-trained with the proposed
Fractal DataBase (FractalDB), a database without natural images, does not
necessarily outperform models pre-trained with human annotated datasets at all
settings, we are able to partially surpass the accuracy of ImageNet/Places
pre-trained models. The image representation with the proposed FractalDB
captures a unique feature in the visualization of convolutional layers and
attentions.