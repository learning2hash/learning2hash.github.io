---
layout: publication
title: 'Matching In The Dark: A Dataset For Matching Image Pairs Of Low-light Scenes'
authors: Wenzheng Song, Masanori Suganuma, Xing Liu, Noriyuki Shimobayashi, Daisuke
  Maruta, Takayuki Okatani
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: song2021matching
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.03585'}]
tags: ["Datasets", "Evaluation", "ICCV"]
short_authors: Song et al.
---
This paper considers matching images of low-light scenes, aiming to widen the
frontier of SfM and visual SLAM applications. Recent image sensors can record
the brightness of scenes with more than eight-bit precision, available in their
RAW-format image. We are interested in making full use of such high-precision
information to match extremely low-light scene images that conventional methods
cannot handle. For extreme low-light scenes, even if some of their brightness
information exists in the RAW format images' low bits, the standard raw image
processing on cameras fails to utilize them properly. As was recently shown by
Chen et al., CNNs can learn to produce images with a natural appearance from
such RAW-format images. To consider if and how well we can utilize such
information stored in RAW-format images for image matching, we have created a
new dataset named MID (matching in the dark). Using it, we experimentally
evaluated combinations of eight image-enhancing methods and eleven image
matching methods consisting of classical/neural local descriptors and
classical/neural initial point-matching methods. The results show the advantage
of using the RAW-format images and the strengths and weaknesses of the above
component methods. They also imply there is room for further research.