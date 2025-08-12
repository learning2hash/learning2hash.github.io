---
layout: publication
title: 'Scenecode: Monocular Dense Semantic Reconstruction Using Learned Encoded Scene
  Representations'
authors: Shuaifeng Zhi, Michael Bloesch, Stefan Leutenegger, Andrew J. Davison
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: zhi2019scenecode
citations: 66
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.06482'}]
tags: ["CVPR"]
short_authors: Zhi et al.
---
Systems which incrementally create 3D semantic maps from image sequences must
store and update representations of both geometry and semantic entities.
However, while there has been much work on the correct formulation for
geometrical estimation, state-of-the-art systems usually rely on simple
semantic representations which store and update independent label estimates for
each surface element (depth pixels, surfels, or voxels). Spatial correlation is
discarded, and fused label maps are incoherent and noisy.
  We introduce a new compact and optimisable semantic representation by
training a variational auto-encoder that is conditioned on a colour image.
Using this learned latent space, we can tackle semantic label fusion by jointly
optimising the low-dimenional codes associated with each of a set of
overlapping images, producing consistent fused label maps which preserve
spatial correlation. We also show how this approach can be used within a
monocular keyframe based semantic mapping system where a similar code approach
is used for geometry. The probabilistic formulation allows a flexible
formulation where we can jointly estimate motion, geometry and semantics in a
unified optimisation.