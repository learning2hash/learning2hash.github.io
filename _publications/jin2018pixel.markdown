---
layout: publication
title: A Pixel-based Framework For Data-driven Clothing
authors: Ning Jin, Yilin Zhu, Zhenglin Geng, Ronald Fedkiw
conference: Computer Graphics Forum
year: 2020
bibkey: jin2018pixel
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.01677'}]
tags: ["Tools & Libraries"]
short_authors: Jin et al.
---
With the aim of creating virtual cloth deformations more similar to real
world clothing, we propose a new computational framework that recasts three
dimensional cloth deformation as an RGB image in a two dimensional pattern
space. Then a three dimensional animation of cloth is equivalent to a sequence
of two dimensional RGB images, which in turn are driven/choreographed via
animation parameters such as joint angles. This allows us to leverage popular
CNNs to learn cloth deformations in image space. The two dimensional cloth
pixels are extended into the real world via standard body skinning techniques,
after which the RGB values are interpreted as texture offsets and displacement
maps. Notably, we illustrate that our approach does not require accurate
unclothed body shapes or robust skinning techniques. Additionally, we discuss
how standard image based techniques such as image partitioning for higher
resolution, GANs for merging partitioned image regions back together, etc., can
readily be incorporated into our framework.