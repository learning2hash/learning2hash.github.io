---
layout: publication
title: 'Guetzli: Perceptually Guided JPEG Encoder'
authors: Jyrki Alakuijala, Robert Obryk, Ostap Stoliarchuk, Zoltan Szabadka, Lode
  Vandevenne, Jan Wassenberg
conference: Arxiv
year: 2017
bibkey: alakuijala2017guetzli
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.04421'}]
tags: ["Quantization"]
short_authors: Alakuijala et al.
---
Guetzli is a new JPEG encoder that aims to produce visually indistinguishable
images at a lower bit-rate than other common JPEG encoders. It optimizes both
the JPEG global quantization tables and the DCT coefficient values in each JPEG
block using a closed-loop optimizer. Guetzli uses Butteraugli, our perceptual
distance metric, as the source of feedback in its optimization process. We
reach a 29-45% reduction in data size for a given perceptual distance,
according to Butteraugli, in comparison to other compressors we tried.
Guetzli's computation is currently extremely slow, which limits its
applicability to compressing static content and serving as a proof- of-concept
that we can achieve significant reductions in size by combining advanced
psychovisual models with lossy compression techniques.