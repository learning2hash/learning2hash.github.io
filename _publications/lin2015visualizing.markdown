---
layout: publication
title: Visualizing And Understanding Deep Texture Representations
authors: Tsung-yu Lin, Subhransu Maji
conference: 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2016
bibkey: lin2015visualizing
citations: 135
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1511.05197'}]
tags: ["CVPR"]
short_authors: Tsung-yu Lin, Subhransu Maji
---
A number of recent approaches have used deep convolutional neural networks
(CNNs) to build texture representations. Nevertheless, it is still unclear how
these models represent texture and invariances to categorical variations. This
work conducts a systematic evaluation of recent CNN-based texture descriptors
for recognition and attempts to understand the nature of invariances captured
by these representations. First we show that the recently proposed bilinear CNN
model [25] is an excellent general-purpose texture descriptor and compares
favorably to other CNN-based descriptors on various texture and scene
recognition benchmarks. The model is translationally invariant and obtains
better accuracy on the ImageNet dataset without requiring spatial jittering of
data compared to corresponding models trained with spatial jittering. Based on
recent work [13, 28] we propose a technique to visualize pre-images, providing
a means for understanding categorical properties that are captured by these
representations. Finally, we show preliminary results on how a unified
parametric model of texture analysis and synthesis can be used for
attribute-based image manipulation, e.g. to make an image more swirly,
honeycombed, or knitted. The source code and additional visualizations are
available at http://vis-www.cs.umass.edu/texture