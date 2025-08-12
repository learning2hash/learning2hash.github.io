---
layout: publication
title: Supervised Classification Methods For Flash X-ray Single Particle Diffraction
  Imaging
authors: Jing Liu, Gijs van Der Schot, Stefan Engblom
conference: Optics Express
year: 2019
bibkey: liu2018supervised
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.10786'}]
tags: ["Supervised"]
short_authors: Jing Liu, Gijs van Der Schot, Stefan Engblom
---
Current Flash X-ray single-particle diffraction Imaging (FXI) experiments,
which operate on modern X-ray Free Electron Lasers (XFELs), can record millions
of interpretable diffraction patterns from individual biomolecules per day. Due
to the stochastic nature of the XFELs, those patterns will to a varying degree
include scatterings from contaminated samples. Also, the heterogeneity of the
sample biomolecules is unavoidable and complicates data processing. Reducing
the data volumes and selecting high-quality single-molecule patterns are
therefore critical steps in the experimental set-up.
  In this paper, we present two supervised template-based learning methods for
classifying FXI patterns. Our Eigen-Image and Log-Likelihood classifier can
find the best-matched template for a single-molecule pattern within a few
milliseconds. It is also straightforward to parallelize them so as to fully
match the XFEL repetition rate, thereby enabling processing at site.