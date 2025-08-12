---
layout: publication
title: 'Deephist: Differentiable Joint And Color Histogram Layers For Image-to-image
  Translation'
authors: Mor Avi-Aharon, Assaf Arbelle, Tammy Riklin Raviv
conference: Arxiv
year: 2020
bibkey: aviaharon2020deephist
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.03995'}]
tags: ["Tools & Libraries"]
short_authors: Mor Avi-Aharon, Assaf Arbelle, Tammy Riklin Raviv
---
We present the DeepHist - a novel Deep Learning framework for augmenting a
network by histogram layers and demonstrate its strength by addressing
image-to-image translation problems. Specifically, given an input image and a
reference color distribution we aim to generate an output image with the
structural appearance (content) of the input (source) yet with the colors of
the reference. The key idea is a new technique for a differentiable
construction of joint and color histograms of the output images. We further
define a color distribution loss based on the Earth Mover's Distance between
the output's and the reference's color histograms and a Mutual Information loss
based on the joint histograms of the source and the output images. Promising
results are shown for the tasks of color transfer, image colorization and edges
\(\rightarrow\) photo, where the color distribution of the output image is
controlled. Comparison to Pix2Pix and CyclyGANs are shown.