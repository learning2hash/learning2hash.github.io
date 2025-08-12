---
layout: publication
title: 'Texture For Colors: Natural Representations Of Colors Using Variable Bit-depth
  Textures'
authors: Shumeet Baluja
conference: Arxiv
year: 2021
bibkey: baluja2021texture
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.01768'}]
tags: []
short_authors: Shumeet Baluja
---
Numerous methods have been proposed to transform color and grayscale images
to their single bit-per-pixel binary counterparts. Commonly, the goal is to
enhance specific attributes of the original image to make it more amenable for
analysis. However, when the resulting binarized image is intended for human
viewing, aesthetics must also be considered. Binarization techniques, such as
half-toning, stippling, and hatching, have been widely used for modeling the
original image's intensity profile. We present an automated method to transform
an image to a set of binary textures that represent not only the intensities,
but also the colors of the original. The foundation of our method is
information preservation: creating a set of textures that allows for the
reconstruction of the original image's colors solely from the binarized
representation. We present techniques to ensure that the textures created are
not visually distracting, preserve the intensity profile of the images, and are
natural in that they map sets of colors that are perceptually similar to
patterns that are similar. The approach uses deep-neural networks and is
entirely self-supervised; no examples of good vs. bad binarizations are
required. The system yields aesthetically pleasing binary images when tested on
a variety of image sources.