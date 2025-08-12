---
layout: publication
title: 'Ninjadesc: Content-concealing Visual Descriptors Via Adversarial Learning'
authors: Tony Ng, Hyo Jin Kim, Vincent Lee, Daniel Detone, Tsun-yi Yang, Tianwei Shen,
  Eddy Ilg, Vassileios Balntas, Krystian Mikolajczyk, Chris Sweeney
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: ng2021ninjadesc
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.12785'}]
tags: ["CVPR", "Robustness"]
short_authors: Ng et al.
---
In the light of recent analyses on privacy-concerning scene revelation from
visual descriptors, we develop descriptors that conceal the input image
content. In particular, we propose an adversarial learning framework for
training visual descriptors that prevent image reconstruction, while
maintaining the matching accuracy. We let a feature encoding network and image
reconstruction network compete with each other, such that the feature encoder
tries to impede the image reconstruction with its generated descriptors, while
the reconstructor tries to recover the input image from the descriptors. The
experimental results demonstrate that the visual descriptors obtained with our
method significantly deteriorate the image reconstruction quality with minimal
impact on correspondence matching and camera localization performance.