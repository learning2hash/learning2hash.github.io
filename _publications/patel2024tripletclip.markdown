---
layout: publication
title: 'Tripletclip: Improving Compositional Reasoning Of CLIP Via Synthetic Vision-language
  Negatives'
authors: Maitreya Patel, Abhiram Kusumba, Sheng Cheng, Changhoon Kim, Tejas Gokhale,
  Chitta Baral, Yezhou Yang
conference: Arxiv
year: 2024
bibkey: patel2024tripletclip
citations: 0
additional_links: [{name: Code, url: 'https://tripletclip.github.io'}, {name: Paper,
    url: 'https://arxiv.org/abs/2411.02545'}]
tags: ["Datasets", "Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Patel et al.
---
Contrastive Language-Image Pretraining (CLIP) models maximize the mutual
information between text and visual modalities to learn representations. This
makes the nature of the training data a significant factor in the efficacy of
CLIP for downstream tasks. However, the lack of compositional diversity in
contemporary image-text datasets limits the compositional reasoning ability of
CLIP. We show that generating ``hard'' negative captions via in-context
learning and synthesizing corresponding negative images with text-to-image
generators offers a solution. We introduce a novel contrastive pre-training
strategy that leverages these hard negative captions and images in an
alternating fashion to train CLIP. We demonstrate that our method, named
TripletCLIP, when applied to existing datasets such as CC3M and CC12M, enhances
the compositional capabilities of CLIP, resulting in an absolute improvement of
over 9% on the SugarCrepe benchmark on an equal computational budget, as well
as improvements in zero-shot image classification and image retrieval. Our
code, models, and data are available at: https://tripletclip.github.io