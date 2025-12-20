---
layout: publication
title: 'Misalign, Contrast Then Distill: Rethinking Misalignments In Language-image
  Pretraining'
authors: Bumsoo Kim, Yeonsik Jo, Jinhyung Kim, Seung Hwan Kim
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: kim2023misalign
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.12661'}]
tags: ["Datasets", "Distance Metric Learning", "Efficiency", "ICCV"]
short_authors: Kim et al.
---
Contrastive Language-Image Pretraining has emerged as a prominent approach
for training vision and text encoders with uncurated image-text pairs from the
web. To enhance data-efficiency, recent efforts have introduced additional
supervision terms that involve random-augmented views of the image. However,
since the image augmentation process is unaware of its text counterpart, this
procedure could cause various degrees of image-text misalignments during
training. Prior methods either disregarded this discrepancy or introduced
external models to mitigate the impact of misalignments during training. In
contrast, we propose a novel metric learning approach that capitalizes on these
misalignments as an additional training source, which we term "Misalign,
Contrast then Distill (MCD)". Unlike previous methods that treat augmented
images and their text counterparts as simple positive pairs, MCD predicts the
continuous scales of misalignment caused by the augmentation. Our extensive
experimental results show that our proposed MCD achieves state-of-the-art
transferability in multiple classification and retrieval downstream datasets.