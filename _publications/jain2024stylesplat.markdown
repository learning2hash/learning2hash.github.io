---
layout: publication
title: 'Stylesplat: 3D Object Style Transfer With Gaussian Splatting'
authors: Sahil Jain, Avik Kuthiala, Prabhdeep Singh Sethi, Prakanshul Saxena
conference: Arxiv
year: 2024
bibkey: jain2024stylesplat
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.09473'}]
tags: []
short_authors: Jain et al.
---
Recent advancements in radiance fields have opened new avenues for creating
high-quality 3D assets and scenes. Style transfer can enhance these 3D assets
with diverse artistic styles, transforming creative expression. However,
existing techniques are often slow or unable to localize style transfer to
specific objects. We introduce StyleSplat, a lightweight method for stylizing
3D objects in scenes represented by 3D Gaussians from reference style images.
Our approach first learns a photorealistic representation of the scene using 3D
Gaussian splatting while jointly segmenting individual 3D objects. We then use
a nearest-neighbor feature matching loss to finetune the Gaussians of the
selected objects, aligning their spherical harmonic coefficients with the style
image to ensure consistency and visual appeal. StyleSplat allows for quick,
customizable style transfer and localized stylization of multiple objects
within a scene, each with a different style. We demonstrate its effectiveness
across various 3D scenes and styles, showcasing enhanced control and
customization in 3D creation.