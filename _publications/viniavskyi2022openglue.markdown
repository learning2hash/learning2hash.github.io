---
layout: publication
title: 'Openglue: Open Source Graph Neural Net Based Pipeline For Image Matching'
authors: Ostap Viniavskyi, Mariia Dobko, Dmytro Mishkin, Oles Dobosevych
conference: Arxiv
year: 2022
bibkey: viniavskyi2022openglue
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.08870'}]
tags: ["Tools & Libraries"]
short_authors: Viniavskyi et al.
---
We present OpenGlue: a free open-source framework for image matching, that
uses a Graph Neural Network-based matcher inspired by SuperGlue
\cite\{sarlin20superglue\}. We show that including additional geometrical
information, such as local feature scale, orientation, and affine geometry,
when available (e.g. for SIFT features), significantly improves the performance
of the OpenGlue matcher. We study the influence of the various attention
mechanisms on accuracy and speed. We also present a simple architectural
improvement by combining local descriptors with context-aware descriptors. The
code and pretrained OpenGlue models for the different local features are
publicly available.