---
layout: publication
title: Annotation Free Semantic Segmentation With Vision Foundation Models
authors: Soroush Seifi, Daniel Olmeda Reino, Fabien Despinoy, Rahaf Aljundi
conference: Arxiv
year: 2024
bibkey: seifi2024annotation
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.09307'}]
tags: []
short_authors: Seifi et al.
---
Semantic Segmentation is one of the most challenging vision tasks, usually
requiring large amounts of training data with expensive pixel level
annotations. With the success of foundation models and especially
vision-language models, recent works attempt to achieve zeroshot semantic
segmentation while requiring either large-scale training or additional
image/pixel level annotations. In this work, we generate free annotations for
any semantic segmentation dataset using existing foundation models. We use CLIP
to detect objects and SAM to generate high quality object masks. Next, we build
a lightweight module on top of a self-supervised vision encoder, DinoV2, to
align the patch features with a pretrained text encoder for zeroshot semantic
segmentation. Our approach can bring language-based semantics to any pretrained
vision encoder with minimal training, uses foundation models as the sole source
of supervision and generalizes from little training data with no annotation.