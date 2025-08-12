---
layout: publication
title: Filtering After Shading With Stochastic Texture Filtering
authors: Matt Pharr, Bartlomiej Wronski, Marco Salvi, Marcos Fajardo
conference: Proceedings of the ACM on Computer Graphics and Interactive Techniques
year: 2024
bibkey: pharr2024filtering
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.06107'}]
tags: []
short_authors: Pharr et al.
---
2D texture maps and 3D voxel arrays are widely used to add rich detail to the
surfaces and volumes of rendered scenes, and filtered texture lookups are
integral to producing high-quality imagery. We show that applying the texture
filter after evaluating shading generally gives more accurate imagery than
filtering textures before BSDF evaluation, as is current practice. These
benefits are not merely theoretical, but are apparent in common cases. We
demonstrate that practical and efficient filtering after shading is possible
through the use of stochastic sampling of texture filters.
  Stochastic texture filtering offers additional benefits, including efficient
implementation of high-quality texture filters and efficient filtering of
textures stored in compressed and sparse data structures, including neural
representations. We demonstrate applications in both real-time and offline
rendering and show that the additional error from stochastic filtering is
minimal. We find that this error is handled well by either spatiotemporal
denoising or moderate pixel sampling rates.