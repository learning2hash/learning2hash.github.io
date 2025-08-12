---
layout: publication
title: 'Deep Shading: Convolutional Neural Networks For Screen-space Shading'
authors: Oliver Nalbach, Elena Arabadzhiyska, Dushyant Mehta, Hans-peter Seidel, Tobias
  Ritschel
conference: Computer Graphics Forum
year: 2017
bibkey: nalbach2016deep
citations: 88
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.06078'}]
tags: []
short_authors: Nalbach et al.
---
In computer vision, convolutional neural networks (CNNs) have recently
achieved new levels of performance for several inverse problems where RGB pixel
appearance is mapped to attributes such as positions, normals or reflectance.
In computer graphics, screen-space shading has recently increased the visual
quality in interactive image synthesis, where per-pixel attributes such as
positions, normals or reflectance of a virtual 3D scene are converted into RGB
pixel appearance, enabling effects like ambient occlusion, indirect light,
scattering, depth-of-field, motion blur, or anti-aliasing. In this paper we
consider the diagonal problem: synthesizing appearance from given per-pixel
attributes using a CNN. The resulting Deep Shading simulates various
screen-space effects at competitive quality and speed while not being
programmed by human experts but learned from example images.