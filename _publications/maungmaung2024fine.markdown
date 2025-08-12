---
layout: publication
title: Fine-tuning Text-to-image Diffusion Models For Class-wise Spurious Feature
  Generation
authors: Aprilpyone Maungmaung, Huy H. Nguyen, Hitoshi Kiya, Isao Echizen
conference: 2024 IEEE International Conference on Image Processing (ICIP)
year: 2024
bibkey: maungmaung2024fine
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.08200'}]
tags: []
short_authors: Maungmaung et al.
---
We propose a method for generating spurious features by leveraging
large-scale text-to-image diffusion models. Although the previous work detects
spurious features in a large-scale dataset like ImageNet and introduces
Spurious ImageNet, we found that not all spurious images are spurious across
different classifiers. Although spurious images help measure the reliance of a
classifier, filtering many images from the Internet to find more spurious
features is time-consuming. To this end, we utilize an existing approach of
personalizing large-scale text-to-image diffusion models with available
discovered spurious images and propose a new spurious feature similarity loss
based on neural features of an adversarially robust model. Precisely, we
fine-tune Stable Diffusion with several reference images from Spurious ImageNet
with a modified objective incorporating the proposed spurious-feature
similarity loss. Experiment results show that our method can generate spurious
images that are consistently spurious across different classifiers. Moreover,
the generated spurious images are visually similar to reference images from
Spurious ImageNet.