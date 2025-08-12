---
layout: publication
title: Learning Geodesic-aware Local Features From RGB-D Images
authors: Guilherme Potje, Renato Martins, Felipe Cadar, Erickson R. Nascimento
conference: Computer Vision and Image Understanding
year: 2022
bibkey: potje2022learning
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.12016'}]
tags: []
short_authors: Potje et al.
---
Most of the existing handcrafted and learning-based local descriptors are
still at best approximately invariant to affine image transformations, often
disregarding deformable surfaces. In this paper, we take one step further by
proposing a new approach to compute descriptors from RGB-D images (where RGB
refers to the pixel color brightness and D stands for depth information) that
are invariant to isometric non-rigid deformations, as well as to scale changes
and rotation. Our proposed description strategies are grounded on the key idea
of learning feature representations on undistorted local image patches using
surface geodesics. We design two complementary local descriptors strategies to
compute geodesic-aware features efficiently: one efficient binary descriptor
based on handcrafted binary tests (named GeoBit), and one learning-based
descriptor (GeoPatch) with convolutional neural networks (CNNs) to compute
features. In different experiments using real and publicly available RGB-D data
benchmarks, they consistently outperforms state-of-the-art handcrafted and
learning-based image and RGB-D descriptors in matching scores, as well as in
object retrieval and non-rigid surface tracking experiments, with comparable
processing times. We also provide to the community a new dataset with accurate
matching annotations of RGB-D images of different objects (shirts, cloths,
paintings, bags), subjected to strong non-rigid deformations, for evaluation
benchmark of deformable surface correspondence algorithms.