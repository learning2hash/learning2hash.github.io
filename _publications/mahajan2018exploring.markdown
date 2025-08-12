---
layout: publication
title: Exploring The Limits Of Weakly Supervised Pretraining
authors: Dhruv Mahajan, Ross Girshick, Vignesh Ramanathan, Kaiming He, Manohar Paluri,
  Yixuan Li, Ashwin Bharambe, Laurens van Der Maaten
conference: Lecture Notes in Computer Science
year: 2018
bibkey: mahajan2018exploring
citations: 1120
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.00932'}]
tags: ["Supervised"]
short_authors: Mahajan et al.
---
State-of-the-art visual perception models for a wide range of tasks rely on
supervised pretraining. ImageNet classification is the de facto pretraining
task for these models. Yet, ImageNet is now nearly ten years old and is by
modern standards "small". Even so, relatively little is known about the
behavior of pretraining with datasets that are multiple orders of magnitude
larger. The reasons are obvious: such datasets are difficult to collect and
annotate. In this paper, we present a unique study of transfer learning with
large convolutional networks trained to predict hashtags on billions of social
media images. Our experiments demonstrate that training for large-scale hashtag
prediction leads to excellent results. We show improvements on several image
classification and object detection tasks, and report the highest ImageNet-1k
single-crop, top-1 accuracy to date: 85.4% (97.6% top-5). We also perform
extensive experiments that provide novel empirical data on the relationship
between large-scale pretraining and transfer learning performance.