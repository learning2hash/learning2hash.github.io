---
layout: publication
title: 'Deepmorph: A System For Hiding Bitstrings In Morphable Vector Drawings'
authors: "S\xF8ren Rasmussen, Karsten \xD8stergaard Noe, Oliver Gyldenberg Hjermitslev,\
  \ Henrik Pedersen"
conference: Arxiv
year: 2020
bibkey: rasmussen2020deepmorph
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.09783'}]
tags: []
short_authors: Rasmussen et al.
---
We introduce DeepMorph, an information embedding technique for vector
drawings. Provided a vector drawing, such as a Scalable Vector Graphics (SVG)
file, our method embeds bitstrings in the image by perturbing the drawing
primitives (lines, circles, etc.). This results in a morphed image that can be
decoded to recover the original bitstring. The use-case is similar to that of
the well-known QR code, but our solution provides creatives with artistic
freedom to transfer digital information via drawings of their own design. The
method comprises two neural networks, which are trained jointly: an encoder
network that transforms a bitstring into a perturbation of the drawing
primitives, and a decoder network that recovers the bitstring from an image of
the morphed drawing. To enable end-to-end training via back propagation, we
introduce a soft rasterizer, which is differentiable with respect to
perturbations of the drawing primitives. In order to add robustness towards
real-world image capture conditions, image corruptions are injected between the
soft rasterizer and the decoder. Further, the addition of an object detection
and camera pose estimation system enables decoding of drawings in complex
scenes as well as use of the drawings as markers for use in augmented reality
applications. We demonstrate that our method reliably recovers bitstrings from
real-world photos of printed drawings, thereby providing a novel solution for
creatives to transfer digital information via artistic imagery.