---
layout: publication
title: Cloth Interactive Transformer For Virtual Try-on
authors: Bin Ren, Hao Tang, Fanyang Meng, Runwei Ding, Philip H. S. Torr, Nicu Sebe
conference: Arxiv
year: 2021
bibkey: ren2021cloth
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.05519'}]
tags: []
short_authors: Ren et al.
---
The 2D image-based virtual try-on has aroused increased interest from the
multimedia and computer vision fields due to its enormous commercial value.
Nevertheless, most existing image-based virtual try-on approaches directly
combine the person-identity representation and the in-shop clothing items
without taking their mutual correlations into consideration. Moreover, these
methods are commonly established on pure convolutional neural networks (CNNs)
architectures which are not simple to capture the long-range correlations among
the input pixels. As a result, it generally results in inconsistent results. To
alleviate these issues, in this paper, we propose a novel two-stage cloth
interactive transformer (CIT) method for the virtual try-on task. During the
first stage, we design a CIT matching block, aiming to precisely capture the
long-range correlations between the cloth-agnostic person information and the
in-shop cloth information. Consequently, it makes the warped in-shop clothing
items look more natural in appearance. In the second stage, we put forth a CIT
reasoning block for establishing global mutual interactive dependencies among
person representation, the warped clothing item, and the corresponding warped
cloth mask. The empirical results, based on mutual dependencies, demonstrate
that the final try-on results are more realistic. Substantial empirical results
on a public fashion dataset illustrate that the suggested CIT attains
competitive virtual try-on performance.