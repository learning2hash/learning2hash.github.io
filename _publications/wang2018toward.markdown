---
layout: publication
title: Toward Characteristic-preserving Image-based Virtual Try-on Network
authors: Bochao Wang, Huabin Zheng, Xiaodan Liang, Yimin Chen, Liang Lin, Meng Yang
conference: Lecture Notes in Computer Science
year: 2018
bibkey: wang2018toward
citations: 356
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.07688'}]
tags: []
short_authors: Wang et al.
---
Image-based virtual try-on systems for fitting new in-shop clothes into a
person image have attracted increasing research attention, yet is still
challenging. A desirable pipeline should not only transform the target clothes
into the most fitting shape seamlessly but also preserve well the clothes
identity in the generated image, that is, the key characteristics (e.g.
texture, logo, embroidery) that depict the original clothes. However, previous
image-conditioned generation works fail to meet these critical requirements
towards the plausible virtual try-on performance since they fail to handle
large spatial misalignment between the input image and target clothes. Prior
work explicitly tackled spatial deformation using shape context matching, but
failed to preserve clothing details due to its coarse-to-fine strategy. In this
work, we propose a new fully-learnable Characteristic-Preserving Virtual Try-On
Network(CP-VTON) for addressing all real-world challenges in this task. First,
CP-VTON learns a thin-plate spline transformation for transforming the in-shop
clothes into fitting the body shape of the target person via a new Geometric
Matching Module (GMM) rather than computing correspondences of interest points
as prior works did. Second, to alleviate boundary artifacts of warped clothes
and make the results more realistic, we employ a Try-On Module that learns a
composition mask to integrate the warped clothes and the rendered image to
ensure smoothness. Extensive experiments on a fashion dataset demonstrate our
CP-VTON achieves the state-of-the-art virtual try-on performance both
qualitatively and quantitatively.