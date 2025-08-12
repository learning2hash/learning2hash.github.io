---
layout: publication
title: Few-shot Object Detection Via Synthetic Features With Optimal Transport
authors: Anh-khoa Nguyen Vu, Thanh-toan Do, Vinh-tiep Nguyen, Tam Le, Minh-triet Tran,
  Tam V. Nguyen
conference: Computer Vision and Image Understanding
year: 2025
bibkey: vu2023few
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.15005'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Vu et al.
---
Few-shot object detection aims to simultaneously localize and classify the
objects in an image with limited training samples. However, most existing
few-shot object detection methods focus on extracting the features of a few
samples of novel classes that lack diversity. Hence, they may not be sufficient
to capture the data distribution. To address that limitation, in this paper, we
propose a novel approach in which we train a generator to generate synthetic
data for novel classes. Still, directly training a generator on the novel class
is not effective due to the lack of novel data. To overcome that issue, we
leverage the large-scale dataset of base classes. Our overarching goal is to
train a generator that captures the data variations of the base dataset. We
then transform the captured variations into novel classes by generating
synthetic data with the trained generator. To encourage the generator to
capture data variations on base classes, we propose to train the generator with
an optimal transport loss that minimizes the optimal transport distance between
the distributions of real and synthetic data. Extensive experiments on two
benchmark datasets demonstrate that the proposed method outperforms the state
of the art. Source code will be available.