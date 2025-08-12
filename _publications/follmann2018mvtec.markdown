---
layout: publication
title: 'Mvtec D2S: Densely Segmented Supermarket Dataset'
authors: "Patrick Follmann, Tobias B\xF6ttger, Philipp H\xE4rtinger, Rebecca K\xF6\
  nig, Markus Ulrich"
conference: Lecture Notes in Computer Science
year: 2018
bibkey: follmann2018mvtec
citations: 71
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.08292'}]
tags: ["Datasets"]
short_authors: Follmann et al.
---
We introduce the Densely Segmented Supermarket (D2S) dataset, a novel
benchmark for instance-aware semantic segmentation in an industrial domain. It
contains 21,000 high-resolution images with pixel-wise labels of all object
instances. The objects comprise groceries and everyday products from 60
categories. The benchmark is designed such that it resembles the real-world
setting of an automatic checkout, inventory, or warehouse system. The training
images only contain objects of a single class on a homogeneous background,
while the validation and test sets are much more complex and diverse. To
further benchmark the robustness of instance segmentation methods, the scenes
are acquired with different lightings, rotations, and backgrounds. We ensure
that there are no ambiguities in the labels and that every instance is labeled
comprehensively. The annotations are pixel-precise and allow using crops of
single instances for articial data augmentation. The dataset covers several
challenges highly relevant in the field, such as a limited amount of training
data and a high diversity in the test and validation sets. The evaluation of
state-of-the-art object detection and instance segmentation methods on D2S
reveals significant room for improvement.