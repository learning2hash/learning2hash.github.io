---
layout: publication
title: Learning Gaussian Data Augmentation In Feature Space For One-shot Object Detection
  In Manga
authors: Takara Taniguchi, Ryosuke Furuta
conference: Arxiv
year: 2024
bibkey: taniguchi2024learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.05935'}]
tags: []
short_authors: Takara Taniguchi, Ryosuke Furuta
---
We tackle one-shot object detection in Japanese Manga. The rising global
popularity of Japanese manga has made the object detection of character faces
increasingly important, with potential applications such as automatic
colorization. However, obtaining sufficient data for training conventional
object detectors is challenging due to copyright restrictions. Additionally,
new characters appear every time a new volume of manga is released, making it
impractical to re-train object detectors each time to detect these new
characters. Therefore, one-shot object detection, where only a single query
(reference) image is required to detect a new character, is an essential task
in the manga industry. One challenge with one-shot object detection in manga is
the large variation in the poses and facial expressions of characters in target
images, despite having only one query image as a reference. Another challenge
is that the frequency of character appearances follows a long-tail
distribution. To overcome these challenges, we propose a data augmentation
method in feature space to increase the variation of the query. The proposed
method augments the feature from the query by adding Gaussian noise, with the
noise variance at each channel learned during training. The experimental
results show that the proposed method improves the performance for both seen
and unseen classes, surpassing data augmentation methods in image space.