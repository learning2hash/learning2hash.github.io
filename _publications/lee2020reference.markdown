---
layout: publication
title: Reference-based Sketch Image Colorization Using Augmented-self Reference And
  Dense Semantic Correspondence
authors: Junsoo Lee, Eungyeup Kim, Yunsung Lee, Dongjun Kim, Jaehyuk Chang, Jaegul
  Choo
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: lee2020reference
citations: 153
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.05207'}]
tags: ["CVPR"]
short_authors: Lee et al.
---
This paper tackles the automatic colorization task of a sketch image given an
already-colored reference image. Colorizing a sketch image is in high demand in
comics, animation, and other content creation applications, but it suffers from
information scarcity of a sketch image. To address this, a reference image can
render the colorization process in a reliable and user-driven manner. However,
it is difficult to prepare for a training data set that has a sufficient amount
of semantically meaningful pairs of images as well as the ground truth for a
colored image reflecting a given reference (e.g., coloring a sketch of an
originally blue car given a reference green car). To tackle this challenge, we
propose to utilize the identical image with geometric distortion as a virtual
reference, which makes it possible to secure the ground truth for a colored
output image. Furthermore, it naturally provides the ground truth for dense
semantic correspondence, which we utilize in our internal attention mechanism
for color transfer from reference to sketch input. We demonstrate the
effectiveness of our approach in various types of sketch image colorization via
quantitative as well as qualitative evaluation against existing methods.