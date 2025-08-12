---
layout: publication
title: Improving Pixel Embedding Learning Through Intermediate Distance Regression
  Supervision For Instance Segmentation
authors: Yuli Wu, Long Chen, Dorit Merhof
conference: Lecture Notes in Computer Science
year: 2020
bibkey: wu2020improving
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.06660'}]
tags: []
short_authors: Yuli Wu, Long Chen, Dorit Merhof
---
As a proposal-free approach, instance segmentation through pixel embedding
learning and clustering is gaining more emphasis. Compared with bounding box
refinement approaches, such as Mask R-CNN, it has potential advantages in
handling complex shapes and dense objects. In this work, we propose a simple,
yet highly effective, architecture for object-aware embedding learning. A
distance regression module is incorporated into our architecture to generate
seeds for fast clustering. At the same time, we show that the features learned
by the distance regression module are able to promote the accuracy of learned
object-aware embeddings significantly. By simply concatenating features of the
distance regression module to the images as inputs of the embedding module, the
mSBD scores on the CVPPP Leaf Segmentation Challenge can be further improved by
more than 8% compared to the identical set-up without concatenation, yielding
the best overall result amongst the leaderboard at CodaLab.