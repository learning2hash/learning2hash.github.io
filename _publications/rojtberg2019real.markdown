---
layout: publication
title: Real-time Texturing For 6D Object Instance Detection From RGB Images
authors: Pavel Rojtberg, Arjan Kuijper
conference: 2019 IEEE International Symposium on Mixed and Augmented Reality Adjunct
  (ISMAR-Adjunct)
year: 2019
bibkey: rojtberg2019real
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.06404'}]
tags: ["Efficiency"]
short_authors: Pavel Rojtberg, Arjan Kuijper
---
For objected detection, the availability of color cues strongly influences
detection rates and is even a prerequisite for many methods. However, when
training on synthetic CAD data, this information is not available. We therefore
present a method for generating a texture-map from image sequences in
real-time. The method relies on 6 degree-of-freedom poses and a 3D-model being
available. In contrast to previous works this allows interleaving detection and
texturing for upgrading the detector on-the-fly. Our evaluation shows that the
acquired texture-map significantly improves detection rates using the LINEMOD
detector on RGB images only. Additionally, we use the texture-map to
differentiate instances of the same object by surface color.