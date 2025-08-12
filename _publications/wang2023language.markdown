---
layout: publication
title: Language-guided Few-shot Semantic Segmentation
authors: Jing Wang, Yuang Liu, Qiang Zhou, Fan Wang
conference: ICASSP 2024 - 2024 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2024
bibkey: wang2023language
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.13865'}]
tags: ["Few Shot & Zero Shot", "ICASSP"]
short_authors: Wang et al.
---
Few-shot learning is a promising way for reducing the label cost in new
categories adaptation with the guidance of a small, well labeled support set.
But for few-shot semantic segmentation, the pixel-level annotations of support
images are still expensive. In this paper, we propose an innovative solution to
tackle the challenge of few-shot semantic segmentation using only language
information, i.e.image-level text labels. Our approach involves a
vision-language-driven mask distillation scheme, which contains a
vision-language pretraining (VLP) model and a mask refiner, to generate high
quality pseudo-semantic masks from text prompts. We additionally introduce a
distributed prototype supervision method and complementary correlation matching
module to guide the model in digging precise semantic relations among support
and query images. The experiments on two benchmark datasets demonstrate that
our method establishes a new baseline for language-guided few-shot semantic
segmentation and achieves competitive results to recent vision-guided methods.