---
layout: publication
title: Foveated Image Processing For Faster Object Detection And Recognition In Embedded
  Systems Using Deep Convolutional Neural Networks
authors: Uziel Jaramillo-Avila, Sean R. Anderson
conference: Lecture Notes in Computer Science
year: 2019
bibkey: jaramilloavila2019foveated
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.09000'}]
tags: []
short_authors: Uziel Jaramillo-Avila, Sean R. Anderson
---
Object detection and recognition algorithms using deep convolutional neural
networks (CNNs) tend to be computationally intensive to implement. This
presents a particular challenge for embedded systems, such as mobile robots,
where the computational resources tend to be far less than for workstations. As
an alternative to standard, uniformly sampled images, we propose the use of
foveated image sampling here to reduce the size of images, which are faster to
process in a CNN due to the reduced number of convolution operations. We
evaluate object detection and recognition on the Microsoft COCO database, using
foveated image sampling at different image sizes, ranging from 416x416 to 96x96
pixels, on an embedded GPU -- an NVIDIA Jetson TX2 with 256 CUDA cores. The
results show that it is possible to achieve a 4x speed-up in frame rates, from
3.59 FPS to 15.24 FPS, using 416x416 and 128x128 pixel images respectively. For
foveated sampling, this image size reduction led to just a small decrease in
recall performance in the foveal region, to 92.0% of the baseline performance
with full-sized images, compared to a significant decrease to 50.1% of baseline
recall performance in uniformly sampled images, demonstrating the advantage of
foveated sampling.