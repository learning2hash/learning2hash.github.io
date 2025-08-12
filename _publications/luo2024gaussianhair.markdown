---
layout: publication
title: 'Gaussianhair: Hair Modeling And Rendering With Light-aware Gaussians'
authors: Haimin Luo, Min Ouyang, Zijun Zhao, Suyi Jiang, Longwen Zhang, Qixuan Zhang,
  Wei Yang, Lan Xu, Jingyi Yu
conference: Arxiv
year: 2024
bibkey: luo2024gaussianhair
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.10483'}]
tags: []
short_authors: Luo et al.
---
Hairstyle reflects culture and ethnicity at first glance. In the digital era,
various realistic human hairstyles are also critical to high-fidelity digital
human assets for beauty and inclusivity. Yet, realistic hair modeling and
real-time rendering for animation is a formidable challenge due to its sheer
number of strands, complicated structures of geometry, and sophisticated
interaction with light. This paper presents GaussianHair, a novel explicit hair
representation. It enables comprehensive modeling of hair geometry and
appearance from images, fostering innovative illumination effects and dynamic
animation capabilities. At the heart of GaussianHair is the novel concept of
representing each hair strand as a sequence of connected cylindrical 3D
Gaussian primitives. This approach not only retains the hair's geometric
structure and appearance but also allows for efficient rasterization onto a 2D
image plane, facilitating differentiable volumetric rendering. We further
enhance this model with the "GaussianHair Scattering Model", adept at
recreating the slender structure of hair strands and accurately capturing their
local diffuse color in uniform lighting. Through extensive experiments, we
substantiate that GaussianHair achieves breakthroughs in both geometric and
appearance fidelity, transcending the limitations encountered in
state-of-the-art methods for hair reconstruction. Beyond representation,
GaussianHair extends to support editing, relighting, and dynamic rendering of
hair, offering seamless integration with conventional CG pipeline workflows.
Complementing these advancements, we have compiled an extensive dataset of real
human hair, each with meticulously detailed strand geometry, to propel further
research in this field.