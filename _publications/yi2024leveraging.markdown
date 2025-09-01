---
layout: publication
title: Leveraging Cross-modal Neighbor Representation For Improved CLIP Classification
authors: Chao Yi, Lu Ren, de-Chuan Zhan, Han-Jia Ye
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: yi2024leveraging
citations: 1
additional_links: [{name: Code, url: 'https://github.com/YCaigogogo/CVPR24-CODER.'},
  {name: Paper, url: 'https://arxiv.org/abs/2404.17753'}]
tags: ["CVPR", "Datasets", "Evaluation", "Few Shot & Zero Shot", "Self-Supervised"]
short_authors: Yi et al.
---
CLIP showcases exceptional cross-modal matching capabilities due to its
training on image-text contrastive learning tasks. However, without specific
optimization for unimodal scenarios, its performance in single-modality feature
extraction might be suboptimal. Despite this, some studies have directly used
CLIP's image encoder for tasks like few-shot classification, introducing a
misalignment between its pre-training objectives and feature extraction
methods. This inconsistency can diminish the quality of the image's feature
representation, adversely affecting CLIP's effectiveness in target tasks. In
this paper, we view text features as precise neighbors of image features in
CLIP's space and present a novel CrOss-moDal nEighbor Representation(CODER)
based on the distance structure between images and their neighbor texts. This
feature extraction method aligns better with CLIP's pre-training objectives,
thereby fully leveraging CLIP's robust cross-modal capabilities. The key to
construct a high-quality CODER lies in how to create a vast amount of
high-quality and diverse texts to match with images. We introduce the Auto Text
Generator(ATG) to automatically generate the required texts in a data-free and
training-free manner. We apply CODER to CLIP's zero-shot and few-shot image
classification tasks. Experiment results across various datasets and models
confirm CODER's effectiveness. Code is available
at:https://github.com/YCaigogogo/CVPR24-CODER.