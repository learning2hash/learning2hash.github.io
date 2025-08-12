---
layout: publication
title: 'SED: A Simple Encoder-decoder For Open-vocabulary Semantic Segmentation'
authors: Bin Xie, Jiale Cao, Jin Xie, Fahad Shahbaz Khan, Yanwei Pang
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: xie2023sed
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.15537'}]
tags: ["CVPR"]
short_authors: Xie et al.
---
Open-vocabulary semantic segmentation strives to distinguish pixels into
different semantic groups from an open set of categories. Most existing methods
explore utilizing pre-trained vision-language models, in which the key is to
adopt the image-level model for pixel-level segmentation task. In this paper,
we propose a simple encoder-decoder, named SED, for open-vocabulary semantic
segmentation, which comprises a hierarchical encoder-based cost map generation
and a gradual fusion decoder with category early rejection. The hierarchical
encoder-based cost map generation employs hierarchical backbone, instead of
plain transformer, to predict pixel-level image-text cost map. Compared to
plain transformer, hierarchical backbone better captures local spatial
information and has linear computational complexity with respect to input size.
Our gradual fusion decoder employs a top-down structure to combine cost map and
the feature maps of different backbone levels for segmentation. To accelerate
inference speed, we introduce a category early rejection scheme in the decoder
that rejects many no-existing categories at the early layer of decoder,
resulting in at most 4.7 times acceleration without accuracy degradation.
Experiments are performed on multiple open-vocabulary semantic segmentation
datasets, which demonstrates the efficacy of our SED method. When using
ConvNeXt-B, our SED method achieves mIoU score of 31.6% on ADE20K with 150
categories at 82 millisecond (\\(ms\\)) per image on a single A6000. We will
release it at https://github.com/xb534/SED.git.