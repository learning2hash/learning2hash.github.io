---
layout: publication
title: End-to-end Person Search Sequentially Trained On Aggregated Dataset
authors: Angelique Loesch, Jaonary Rabarisoa, Romaric Audigier
conference: 2019 IEEE International Conference on Image Processing (ICIP)
year: 2019
bibkey: loesch2019end
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.09604'}]
tags: ["Datasets", "Evaluation"]
short_authors: Angelique Loesch, Jaonary Rabarisoa, Romaric Audigier
---
In video surveillance applications, person search is a challenging task
consisting in detecting people and extracting features from their silhouette
for re-identification (re-ID) purpose. We propose a new end-to-end model that
jointly computes detection and feature extraction steps through a single deep
Convolutional Neural Network architecture. Sharing feature maps between the two
tasks for jointly describing people commonalities and specificities allows
faster runtime, which is valuable in real-world applications. In addition to
reaching state-of-the-art accuracy, this multi-task model can be sequentially
trained task-by-task, which results in a broader acceptance of input dataset
types. Indeed, we show that aggregating more pedestrian detection datasets
without costly identity annotations makes the shared feature maps more generic,
and improves re-ID precision. Moreover, these boosted shared feature maps
result in re-ID features more robust to a cross-dataset scenario.