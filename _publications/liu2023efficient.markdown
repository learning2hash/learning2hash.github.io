---
layout: publication
title: Efficient Feature Distillation For Zero-shot Annotation Object Detection
authors: Zhuoming Liu, Xuefeng Hu, Ram Nevatia
conference: 2024 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2024
bibkey: liu2023efficient
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.12145'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Zhuoming Liu, Xuefeng Hu, Ram Nevatia
---
We propose a new setting for detecting unseen objects called Zero-shot
Annotation object Detection (ZAD). It expands the zero-shot object detection
setting by allowing the novel objects to exist in the training images and
restricts the additional information the detector uses to novel category names.
Recently, to detect unseen objects, large-scale vision-language models (e.g.,
CLIP) are leveraged by different methods. The distillation-based methods have
good overall performance but suffer from a long training schedule caused by two
factors. First, existing work creates distillation regions biased to the base
categories, which limits the distillation of novel category information.
Second, directly using the raw feature from CLIP for distillation neglects the
domain gap between the training data of CLIP and the detection datasets, which
makes it difficult to learn the mapping from the image region to the
vision-language feature space. To solve these problems, we propose Efficient
feature distillation for Zero-shot Annotation object Detection (EZAD). Firstly,
EZAD adapts the CLIP's feature space to the target detection domain by
re-normalizing CLIP; Secondly, EZAD uses CLIP to generate distillation
proposals with potential novel category names to avoid the distillation being
overly biased toward the base categories. Finally, EZAD takes advantage of
semantic meaning for regression to further improve the model performance. As a
result, EZAD outperforms the previous distillation-based methods in COCO by 4%
with a much shorter training schedule and achieves a 3% improvement on the LVIS
dataset. Our code is available at https://github.com/dragonlzm/EZAD