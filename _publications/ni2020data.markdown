---
layout: publication
title: Data Augmentation For Meta-learning
authors: Renkun Ni, Micah Goldblum, Amr Sharaf, Kezhi Kong, Tom Goldstein
conference: Arxiv
year: 2020
bibkey: ni2020data
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.07092'}]
tags: ["Evaluation", "Few Shot & Zero Shot"]
short_authors: Ni et al.
---
Conventional image classifiers are trained by randomly sampling mini-batches
of images. To achieve state-of-the-art performance, practitioners use
sophisticated data augmentation schemes to expand the amount of training data
available for sampling. In contrast, meta-learning algorithms sample support
data, query data, and tasks on each training step. In this complex sampling
scenario, data augmentation can be used not only to expand the number of images
available per class, but also to generate entirely new classes/tasks. We
systematically dissect the meta-learning pipeline and investigate the distinct
ways in which data augmentation can be integrated at both the image and class
levels. Our proposed meta-specific data augmentation significantly improves the
performance of meta-learners on few-shot classification benchmarks.