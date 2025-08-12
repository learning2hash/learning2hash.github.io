---
layout: publication
title: 'Dress Code: High-resolution Multi-category Virtual Try-on'
authors: Davide Morelli, Matteo Fincato, Marcella Cornia, Federico Landi, Fabio Cesari,
  Rita Cucchiara
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2022
bibkey: morelli2022dress
citations: 52
additional_links: [{name: Code, url: 'https://github.com/aimagelab/dress-code'}, {
    name: Paper, url: 'https://arxiv.org/abs/2204.08532'}]
tags: ["CVPR"]
short_authors: Morelli et al.
---
Image-based virtual try-on strives to transfer the appearance of a clothing
item onto the image of a target person. Prior work focuses mainly on upper-body
clothes (e.g. t-shirts, shirts, and tops) and neglects full-body or lower-body
items. This shortcoming arises from a main factor: current publicly available
datasets for image-based virtual try-on do not account for this variety, thus
limiting progress in the field. To address this deficiency, we introduce Dress
Code, which contains images of multi-category clothes. Dress Code is more than
3x larger than publicly available datasets for image-based virtual try-on and
features high-resolution paired images (1024x768) with front-view, full-body
reference models. To generate HD try-on images with high visual quality and
rich in details, we propose to learn fine-grained discriminating features.
Specifically, we leverage a semantic-aware discriminator that makes predictions
at pixel-level instead of image- or patch-level. Extensive experimental
evaluation demonstrates that the proposed approach surpasses the baselines and
state-of-the-art competitors in terms of visual quality and quantitative
results. The Dress Code dataset is publicly available at
https://github.com/aimagelab/dress-code.