---
layout: publication
title: 'Deepsurfels: Learning Online Appearance Fusion'
authors: Marko Mihajlovic, Silvan Weder, Marc Pollefeys, Martin R. Oswald
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: mihajlovic2020deepsurfels
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.14240'}]
tags: ["CVPR"]
short_authors: Mihajlovic et al.
---
We present DeepSurfels, a novel hybrid scene representation for geometry and
appearance information. DeepSurfels combines explicit and neural building
blocks to jointly encode geometry and appearance information. In contrast to
established representations, DeepSurfels better represents high-frequency
textures, is well-suited for online updates of appearance information, and can
be easily combined with machine learning methods. We further present an
end-to-end trainable online appearance fusion pipeline that fuses information
from RGB images into the proposed scene representation and is trained using
self-supervision imposed by the reprojection error with respect to the input
images. Our method compares favorably to classical texture mapping approaches
as well as recent learning-based techniques. Moreover, we demonstrate lower
runtime, im-proved generalization capabilities, and better scalability to
larger scenes compared to existing methods.