---
layout: publication
title: 'Imagesig: A Signature Transform For Ultra-lightweight Image Recognition'
authors: Mohamed R. Ibrahim, Terry Lyons
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2022
bibkey: ibrahim2022imagesig
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.06929'}]
tags: ["CVPR", "Efficiency"]
short_authors: Mohamed R. Ibrahim, Terry Lyons
---
This paper introduces a new lightweight method for image recognition.
ImageSig is based on computing signatures and does not require a convolutional
structure or an attention-based encoder. It is striking to the authors that it
achieves: a) an accuracy for 64 X 64 RGB images that exceeds many of the
state-of-the-art methods and simultaneously b) requires orders of magnitude
less FLOPS, power and memory footprint. The pretrained model can be as small as
44.2 KB in size. ImageSig shows unprecedented performance on hardware such as
Raspberry Pi and Jetson-nano. ImageSig treats images as streams with multiple
channels. These streams are parameterized by spatial directions. We contribute
to the functionality of signature and rough path theory to stream-like data and
vision tasks on static images beyond temporal streams. With very few parameters
and small size models, the key advantage is that one could have many of these
"detectors" assembled on the same chip; moreover, the feature acquisition can
be performed once and shared between different models of different tasks -
further accelerating the process. This contributes to energy efficiency and the
advancements of embedded AI at the edge.