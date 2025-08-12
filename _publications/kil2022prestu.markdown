---
layout: publication
title: 'Prestu: Pre-training For Scene-text Understanding'
authors: Jihyung Kil, Soravit Changpinyo, Xi Chen, Hexiang Hu, Sebastian Goodman,
  Wei-lun Chao, Radu Soricut
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: kil2022prestu
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.05534'}]
tags: ["ICCV"]
short_authors: Kil et al.
---
The ability to recognize and reason about text embedded in visual inputs is
often lacking in vision-and-language (V&L) models, perhaps because V&L
pre-training methods have often failed to include such an ability in their
training objective. In this paper, we propose PreSTU, a novel pre-training
recipe dedicated to scene-text understanding (STU). PreSTU introduces OCR-aware
pre-training objectives that encourage the model to recognize text from an
image and connect it to the rest of the image content. We implement PreSTU
using a simple transformer-based encoder-decoder architecture, combined with
large-scale image-text datasets with scene text obtained from an off-the-shelf
OCR system. We empirically demonstrate the effectiveness of this pre-training
approach on eight visual question answering and four image captioning
benchmarks.