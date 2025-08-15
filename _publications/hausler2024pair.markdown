---
layout: publication
title: 'Pair-vpr: Place-aware Pre-training And Contrastive Pair Classification For
  Visual Place Recognition With Vision Transformers'
authors: Stephen Hausler, Peyman Moghadam
conference: IEEE Robotics and Automation Letters
year: 2025
bibkey: hausler2024pair
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.06614'}]
tags: ["Datasets", "Evaluation", "Re-Ranking"]
short_authors: Stephen Hausler, Peyman Moghadam
---
In this work we propose a novel joint training method for Visual Place
Recognition (VPR), which simultaneously learns a global descriptor and a pair
classifier for re-ranking. The pair classifier can predict whether a given pair
of images are from the same place or not. The network only comprises Vision
Transformer components for both the encoder and the pair classifier, and both
components are trained using their respective class tokens. In existing VPR
methods, typically the network is initialized using pre-trained weights from a
generic image dataset such as ImageNet. In this work we propose an alternative
pre-training strategy, by using Siamese Masked Image Modelling as a
pre-training task. We propose a Place-aware image sampling procedure from a
collection of large VPR datasets for pre-training our model, to learn visual
features tuned specifically for VPR. By re-using the Mask Image Modelling
encoder and decoder weights in the second stage of training, Pair-VPR can
achieve state-of-the-art VPR performance across five benchmark datasets with a
ViT-B encoder, along with further improvements in localization recall with
larger encoders. The Pair-VPR website is:
https://csiro-robotics.github.io/Pair-VPR.