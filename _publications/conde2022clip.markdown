---
layout: publication
title: 'Clip-art: Contrastive Pre-training For Fine-grained Art Classification'
authors: Marcos V. Conde, Kerem Turgutlu
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2022
bibkey: conde2022clip
citations: 88
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.14244'}]
tags: ["Datasets", "Few Shot & Zero Shot", "Image Retrieval", "Self-Supervised"]
short_authors: Marcos V. Conde, Kerem Turgutlu
---
Existing computer vision research in artwork struggles with artwork's
fine-grained attributes recognition and lack of curated annotated datasets due
to their costly creation. To the best of our knowledge, we are one of the first
methods to use CLIP (Contrastive Language-Image Pre-Training) to train a neural
network on a variety of artwork images and text descriptions pairs. CLIP is
able to learn directly from free-form art descriptions, or, if available,
curated fine-grained labels. Model's zero-shot capability allows predicting
accurate natural language description for a given image, without directly
optimizing for the task. Our approach aims to solve 2 challenges: instance
retrieval and fine-grained artwork attribute recognition. We use the iMet
Dataset, which we consider the largest annotated artwork dataset. In this
benchmark we achieved competitive results using only self-supervision.