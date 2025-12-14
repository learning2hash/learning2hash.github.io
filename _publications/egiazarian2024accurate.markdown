---
layout: publication
title: Accurate Compression Of Text-to-image Diffusion Models Via Vector Quantization
authors: Vage Egiazarian, Denis Kuznedelev, Anton Voronov, Ruslan Svirschevski, Michael
  Goin, Daniil Pavlov, Dan Alistarh, Dmitry Baranchuk
conference: Arxiv
year: 2024
bibkey: egiazarian2024accurate
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.00492'}]
tags: [Compact Codes, Evaluation, Quantization, Scalability, Tools & Libraries, Large-Scale
    Search]
short_authors: Egiazarian et al.
---
Text-to-image diffusion models have emerged as a powerful framework for
high-quality image generation given textual prompts. Their success has driven
the rapid development of production-grade diffusion models that consistently
increase in size and already contain billions of parameters. As a result,
state-of-the-art text-to-image models are becoming less accessible in practice,
especially in resource-limited environments. Post-training quantization (PTQ)
tackles this issue by compressing the pretrained model weights into lower-bit
representations. Recent diffusion quantization techniques primarily rely on
uniform scalar quantization, providing decent performance for the models
compressed to 4 bits. This work demonstrates that more versatile vector
quantization (VQ) may achieve higher compression rates for large-scale
text-to-image diffusion models. Specifically, we tailor vector-based PTQ
methods to recent billion-scale text-to-image models (SDXL and SDXL-Turbo), and
show that the diffusion models of 2B+ parameters compressed to around 3 bits
using VQ exhibit the similar image quality and textual alignment as previous
4-bit compression techniques.