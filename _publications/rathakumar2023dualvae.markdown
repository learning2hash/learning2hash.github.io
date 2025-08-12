---
layout: publication
title: 'Dualvae: Controlling Colours Of Generated And Real Images'
authors: Keerth Rathakumar, David Liebowitz, Christian Walder, Kristen Moore, Salil
  S. Kanhere
conference: Arxiv
year: 2023
bibkey: rathakumar2023dualvae
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.18769'}]
tags: []
short_authors: Rathakumar et al.
---
Colour controlled image generation and manipulation are of interest to
artists and graphic designers. Vector Quantised Variational AutoEncoders
(VQ-VAEs) with autoregressive (AR) prior are able to produce high quality
images, but lack an explicit representation mechanism to control colour
attributes. We introduce DualVAE, a hybrid representation model that provides
such control by learning disentangled representations for colour and geometry.
The geometry is represented by an image intensity mapping that identifies
structural features. The disentangled representation is obtained by two novel
mechanisms:
  (i) a dual branch architecture that separates image colour attributes from
geometric attributes, and (ii) a new ELBO that trains the combined colour and
geometry representations. DualVAE can control the colour of generated images,
and recolour existing images by transferring the colour latent representation
obtained from an exemplar image. We demonstrate that DualVAE generates images
with FID nearly two times better than VQ-GAN on a diverse collection of
datasets, including animated faces, logos and artistic landscapes.