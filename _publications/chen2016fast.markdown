---
layout: publication
title: Fast Patch-based Style Transfer Of Arbitrary Style
authors: Tian Qi Chen, Mark Schmidt
conference: Arxiv
year: 2016
bibkey: chen2016fast
citations: 220
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.04337'}]
tags: []
short_authors: Tian Qi Chen, Mark Schmidt
---
Artistic style transfer is an image synthesis problem where the content of an
image is reproduced with the style of another. Recent works show that a
visually appealing style transfer can be achieved by using the hidden
activations of a pretrained convolutional neural network. However, existing
methods either apply (i) an optimization procedure that works for any style
image but is very expensive, or (ii) an efficient feedforward network that only
allows a limited number of trained styles. In this work we propose a simpler
optimization objective based on local matching that combines the content
structure and style textures in a single layer of the pretrained network. We
show that our objective has desirable properties such as a simpler optimization
landscape, intuitive parameter tuning, and consistent frame-by-frame
performance on video. Furthermore, we use 80,000 natural images and 80,000
paintings to train an inverse network that approximates the result of the
optimization. This results in a procedure for artistic style transfer that is
efficient but also allows arbitrary content and style images.