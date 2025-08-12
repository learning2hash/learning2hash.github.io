---
layout: publication
title: 'Actorsnerf: Animatable Few-shot Human Rendering With Generalizable Nerfs'
authors: Jiteng Mu, Shen Sang, Nuno Vasconcelos, Xiaolong Wang
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: mu2023actorsnerf
citations: 15
additional_links: [{name: Code, url: 'https://jitengmu.github.io/ActorsNeRF/'}, {
    name: Paper, url: 'https://arxiv.org/abs/2304.14401'}]
tags: ["Few Shot & Zero Shot", "ICCV"]
short_authors: Mu et al.
---
While NeRF-based human representations have shown impressive novel view
synthesis results, most methods still rely on a large number of images / views
for training. In this work, we propose a novel animatable NeRF called
ActorsNeRF. It is first pre-trained on diverse human subjects, and then adapted
with few-shot monocular video frames for a new actor with unseen poses.
Building on previous generalizable NeRFs with parameter sharing using a ConvNet
encoder, ActorsNeRF further adopts two human priors to capture the large human
appearance, shape, and pose variations. Specifically, in the encoded feature
space, we will first align different human subjects in a category-level
canonical space, and then align the same human from different frames in an
instance-level canonical space for rendering. We quantitatively and
qualitatively demonstrate that ActorsNeRF significantly outperforms the
existing state-of-the-art on few-shot generalization to new people and poses on
multiple datasets. Project Page: https://jitengmu.github.io/ActorsNeRF/