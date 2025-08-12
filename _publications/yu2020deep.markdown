---
layout: publication
title: Deep Fusion Siamese Network For Automatic Kinship Verification
authors: Jun Yu, Mengyan Li, Xinlong Hao, Guochen Xie
conference: 2020 15th IEEE International Conference on Automatic Face and Gesture
  Recognition (FG 2020)
year: 2020
bibkey: yu2020deep
citations: 26
additional_links: [{name: Code, url: 'https://github.com/gniknoil/FG2020-kinship'},
  {name: Paper, url: 'https://arxiv.org/abs/2006.00143'}]
tags: []
short_authors: Yu et al.
---
Automatic kinship verification aims to determine whether some individuals
belong to the same family. It is of great research significance to help missing
persons reunite with their families. In this work, the challenging problem is
progressively addressed in two respects. First, we propose a deep siamese
network to quantify the relative similarity between two individuals. When given
two input face images, the deep siamese network extracts the features from them
and fuses these features by combining and concatenating. Then, the fused
features are fed into a fully-connected network to obtain the similarity score
between two faces, which is used to verify the kinship. To improve the
performance, a jury system is also employed for multi-model fusion. Second, two
deep siamese networks are integrated into a deep triplet network for
tri-subject (i.e., father, mother and child) kinship verification, which is
intended to decide whether a child is related to a pair of parents or not.
Specifically, the obtained similarity scores of father-child and mother-child
are weighted to generate the parent-child similarity score for kinship
verification. Recognizing Families In the Wild (RFIW) is a challenging kinship
recognition task with multiple tracks, which is based on Families in the Wild
(FIW), a large-scale and comprehensive image database for automatic kinship
recognition. The Kinship Verification (track I) and Tri-Subject Verification
(track II) are supported during the ongoing RFIW2020 Challenge. Our team
(ustc-nelslip) ranked 1st in track II, and 3rd in track I. The code is
available at https://github.com/gniknoil/FG2020-kinship.