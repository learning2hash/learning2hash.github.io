---
layout: publication
title: Ganx -- Generate Artificially New XRF A Python Library To Generate MA-XRF Raw
  Data Out Of RGB Images
authors: Alessandro Bombini
conference: Arxiv
year: 2023
bibkey: bombini2023ganx
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.14078'}]
tags: ["Tools & Libraries"]
short_authors: Alessandro Bombini
---
In this paper we present the first version of ganX -- generate artificially
new XRF, a Python library to generate X-ray fluorescence Macro maps (MA-XRF)
from a coloured RGB image. To do that, a Monte Carlo method is used, where each
MA-XRF pixel signal is sampled out of an XRF signal probability function. Such
probability function is computed using a database of couples (pigment
characteristic XRF signal, RGB), by a weighted sum of such pigment XRF signal
by proximity of the image RGB to the pigment characteristic RGB. The library is
released to PyPi and the code is available open source on GitHub.