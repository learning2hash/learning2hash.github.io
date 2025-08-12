---
layout: publication
title: 'Tryongan: Body-aware Try-on Via Layered Interpolation'
authors: Kathleen M Lewis, Srivatsan Varadharajan, Ira Kemelmacher-Shlizerman
conference: Arxiv
year: 2021
bibkey: lewis2021tryongan
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.02285'}]
tags: []
short_authors: Kathleen M Lewis, Srivatsan Varadharajan, Ira Kemelmacher-Shlizerman
---
Given a pair of images-target person and garment on another person-we
automatically generate the target person in the given garment. Previous methods
mostly focused on texture transfer via paired data training, while overlooking
body shape deformations, skin color, and seamless blending of garment with the
person. This work focuses on those three components, while also not requiring
paired data training. We designed a pose conditioned StyleGAN2 architecture
with a clothing segmentation branch that is trained on images of people wearing
garments. Once trained, we propose a new layered latent space interpolation
method that allows us to preserve and synthesize skin color and target body
shape while transferring the garment from a different person. We demonstrate
results on high resolution 512x512 images, and extensively compare to state of
the art in try-on on both latent space generated and real images.