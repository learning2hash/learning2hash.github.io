---
layout: publication
title: 'Pic2word: Mapping Pictures To Words For Zero-shot Composed Image Retrieval'
authors: Kuniaki Saito, Kihyuk Sohn, Xiang Zhang, Chun-Liang Li, Chen-Yu Lee, Kate
  Saenko, Tomas Pfister
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: saito2023pic2word
citations: 51
additional_links: [{name: Code, url: 'https://github.com/google-research/composed_image_retrieval'},
  {name: Paper, url: 'https://arxiv.org/abs/2302.03084'}]
tags: ["CVPR", "Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Saito et al.
---
In Composed Image Retrieval (CIR), a user combines a query image with text to
describe their intended target. Existing methods rely on supervised learning of
CIR models using labeled triplets consisting of the query image, text
specification, and the target image. Labeling such triplets is expensive and
hinders broad applicability of CIR. In this work, we propose to study an
important task, Zero-Shot Composed Image Retrieval (ZS-CIR), whose goal is to
build a CIR model without requiring labeled triplets for training. To this end,
we propose a novel method, called Pic2Word, that requires only weakly labeled
image-caption pairs and unlabeled image datasets to train. Unlike existing
supervised CIR models, our model trained on weakly labeled or unlabeled
datasets shows strong generalization across diverse ZS-CIR tasks, e.g.,
attribute editing, object composition, and domain conversion. Our approach
outperforms several supervised CIR methods on the common CIR benchmark, CIRR
and Fashion-IQ. Code will be made publicly available at
https://github.com/google-research/composed_image_retrieval.