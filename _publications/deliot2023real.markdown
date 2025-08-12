---
layout: publication
title: Real-time Rendering Of Glinty Appearances Using Distributed Binomial Laws On
  Anisotropic Grids
authors: Deliot, Thomas, Belcour, Laurent
conference: Computer Graphics Forum
year: 2023
bibkey: deliot2023real
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.05051'}]
tags: ["Efficiency"]
short_authors: Deliot et al.
---
In this work, we render in real-time glittery materials caused by discrete
flakes on the surface. To achieve this, one has to count the number of flakes
reflecting the light towards the camera within every texel covered by a given
pixel footprint. To do so, we derive a counting method for arbitrary footprints
that, unlike previous work, outputs the correct statistics. We combine this
counting method with an anisotropic parameterization of the texture space that
reduces the number of texels falling under a pixel footprint. This allows our
method to run with both stable performance and 1.5X to 5X faster than the
state-of-the-art.