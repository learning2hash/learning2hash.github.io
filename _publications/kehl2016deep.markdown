---
layout: publication
title: Deep Learning Of Local RGB-D Patches For 3D Object Detection And 6D Pose Estimation
authors: Wadim Kehl, Fausto Milletari, Federico Tombari, Slobodan Ilic, Nassir Navab
conference: Lecture Notes in Computer Science
year: 2016
bibkey: kehl2016deep
citations: 288
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1607.06038'}]
tags: ["Datasets"]
short_authors: Kehl et al.
---
We present a 3D object detection method that uses regressed descriptors of
locally-sampled RGB-D patches for 6D vote casting. For regression, we employ a
convolutional auto-encoder that has been trained on a large collection of
random local patches. During testing, scene patch descriptors are matched
against a database of synthetic model view patches and cast 6D object votes
which are subsequently filtered to refined hypotheses. We evaluate on three
datasets to show that our method generalizes well to previously unseen input
data, delivers robust detection results that compete with and surpass the
state-of-the-art while being scalable in the number of objects.