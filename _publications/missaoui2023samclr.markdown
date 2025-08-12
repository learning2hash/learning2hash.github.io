---
layout: publication
title: 'SAMCLR: Contrastive Pre-training On Complex Scenes Using SAM For View Sampling'
authors: Benjamin Missaoui, Chongbin Yuan
conference: Arxiv
year: 2023
bibkey: missaoui2023samclr
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.14736'}]
tags: ["Self-Supervised"]
short_authors: Benjamin Missaoui, Chongbin Yuan
---
In Computer Vision, self-supervised contrastive learning enforces similar
representations between different views of the same image. The pre-training is
most often performed on image classification datasets, like ImageNet, where
images mainly contain a single class of objects. However, when dealing with
complex scenes with multiple items, it becomes very unlikely for several views
of the same image to represent the same object category. In this setting, we
propose SAMCLR, an add-on to SimCLR which uses SAM to segment the image into
semantic regions, then sample the two views from the same region. Preliminary
results show empirically that when pre-training on Cityscapes and ADE20K, then
evaluating on classification on CIFAR-10, STL10 and ImageNette, SAMCLR performs
at least on par with, and most often significantly outperforms not only SimCLR,
but also DINO and MoCo.