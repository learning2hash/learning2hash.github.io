---
layout: publication
title: 'Product-level Try-on: Characteristics-preserving Try-on With Realistic Clothes
  Shading And Wrinkles'
authors: Yanlong Zang, Han Yang, Jiaxu Miao, Yi Yang
conference: Arxiv
year: 2024
bibkey: zang2024product
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.11239'}]
tags: []
short_authors: Zang et al.
---
Image-based virtual try-on systems,which fit new garments onto human
portraits,are gaining research attention.An ideal pipeline should preserve the
static features of clothes(like textures and logos)while also generating
dynamic elements(e.g.shadows,folds)that adapt to the model's pose and
environment.Previous works fail specifically in generating dynamic features,as
they preserve the warped in-shop clothes trivially with predicted an alpha mask
by composition.To break the dilemma of over-preserving and textures losses,we
propose a novel diffusion-based Product-level virtual try-on pipeline,\ie
PLTON, which can preserve the fine details of logos and embroideries while
producing realistic clothes shading and wrinkles.The main insights are in three
folds:1)Adaptive Dynamic Rendering:We take a pre-trained diffusion model as a
generative prior and tame it with image features,training a dynamic extractor
from scratch to generate dynamic tokens that preserve high-fidelity semantic
information. Due to the strong generative power of the diffusion prior,we can
generate realistic clothes shadows and wrinkles.2)Static Characteristics
Transformation: High-frequency Map(HF-Map)is our fundamental insight for static
representation.PLTON first warps in-shop clothes to the target model pose by a
traditional warping network,and uses a high-pass filter to extract an HF-Map
for preserving static cloth features.The HF-Map is used to generate modulation
maps through our static extractor,which are injected into a fixed U-net to
synthesize the final result.To enhance retention,a Two-stage Blended Denoising
method is proposed to guide the diffusion process for correct spatial layout
and color.PLTON is finetuned only with our collected small-size try-on
dataset.Extensive quantitative and qualitative experiments on 1024 768 datasets
demonstrate the superiority of our framework in mimicking real clothes
dynamics.