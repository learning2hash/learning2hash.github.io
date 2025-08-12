---
layout: publication
title: 'Multiscene: A Large-scale Dataset And Benchmark For Multi-scene Recognition
  In Single Aerial Images'
authors: Yuansheng Hua, Lichao Mou, Pu Jin, Xiao Xiang Zhu
conference: Arxiv
year: 2021
bibkey: hua2021multiscene
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.02846'}]
tags: ["Datasets", "Evaluation"]
short_authors: Hua et al.
---
Aerial scene recognition is a fundamental research problem in interpreting
high-resolution aerial imagery. Over the past few years, most studies focus on
classifying an image into one scene category, while in real-world scenarios, it
is more often that a single image contains multiple scenes. Therefore, in this
paper, we investigate a more practical yet underexplored task -- multi-scene
recognition in single images. To this end, we create a large-scale dataset,
called MultiScene, composed of 100,000 unconstrained high-resolution aerial
images. Considering that manually labeling such images is extremely arduous, we
resort to low-cost annotations from crowdsourcing platforms, e.g.,
OpenStreetMap (OSM). However, OSM data might suffer from incompleteness and
incorrectness, which introduce noise into image labels. To address this issue,
we visually inspect 14,000 images and correct their scene labels, yielding a
subset of cleanly-annotated images, named MultiScene-Clean. With it, we can
develop and evaluate deep networks for multi-scene recognition using clean
data. Moreover, we provide crowdsourced annotations of all images for the
purpose of studying network learning with noisy labels. We conduct experiments
with extensive baseline models on both MultiScene-Clean and MultiScene to offer
benchmarks for multi-scene recognition in single images and learning from noisy
labels for this task, respectively. To facilitate progress, we make our dataset
and trained models available on
https://gitlab.lrz.de/ai4eo/reasoning/multiscene.