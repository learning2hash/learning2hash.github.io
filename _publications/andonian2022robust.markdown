---
layout: publication
title: Robust Cross-modal Representation Learning With Progressive Self-distillation
authors: Alex Andonian, Shixing Chen, Raffay Hamid
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: andonian2022robust
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.04588'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Robustness", "Text Retrieval"]
short_authors: Alex Andonian, Shixing Chen, Raffay Hamid
---
The learning objective of vision-language approach of CLIP does not
effectively account for the noisy many-to-many correspondences found in
web-harvested image captioning datasets, which contributes to its compute and
data inefficiency. To address this challenge, we introduce a novel training
framework based on cross-modal contrastive learning that uses progressive
self-distillation and soft image-text alignments to more efficiently learn
robust representations from noisy data. Our model distills its own knowledge to
dynamically generate soft-alignment targets for a subset of images and captions
in every minibatch, which are then used to update its parameters. Extensive
evaluation across 14 benchmark datasets shows that our method consistently
outperforms its CLIP counterpart in multiple settings, including: (a) zero-shot
classification, (b) linear probe transfer, and (c) image-text retrieval,
without incurring added computational cost. Analysis using an ImageNet-based
robustness test-bed reveals that our method offers better effective robustness
to natural distribution shifts compared to both ImageNet-trained models and
CLIP itself. Lastly, pretraining with datasets spanning two orders of magnitude
in size shows that our improvements over CLIP tend to scale with number of
training examples.