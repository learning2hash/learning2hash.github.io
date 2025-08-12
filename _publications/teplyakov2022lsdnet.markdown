---
layout: publication
title: 'Lsdnet: Trainable Modification Of LSD Algorithm For Real-time Line Segment
  Detection'
authors: Lev Teplyakov, Leonid Erlygin, Evgeny Shvets
conference: IEEE Access
year: 2022
bibkey: teplyakov2022lsdnet
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.04642'}]
tags: ["Efficiency"]
short_authors: Lev Teplyakov, Leonid Erlygin, Evgeny Shvets
---
As of today, the best accuracy in line segment detection (LSD) is achieved by
algorithms based on convolutional neural networks - CNNs. Unfortunately, these
methods utilize deep, heavy networks and are slower than traditional
model-based detectors. In this paper we build an accurate yet fast CNN- based
detector, LSDNet, by incorporating a lightweight CNN into a classical LSD
detector. Specifically, we replace the first step of the original LSD algorithm
- construction of line segments heatmap and tangent field from raw image
gradients - with a lightweight CNN, which is able to calculate more complex and
rich features. The second part of the LSD algorithm is used with only minor
modifications. Compared with several modern line segment detectors on standard
Wireframe dataset, the proposed LSDNet provides the highest speed (among
CNN-based detectors) of 214 FPS with a competitive accuracy of 78 Fh . Although
the best-reported accuracy is 83 Fh at 33 FPS, we speculate that the observed
accuracy gap is caused by errors in annotations and the actual gap is
significantly lower. We point out systematic inconsistencies in the annotations
of popular line detection benchmarks - Wireframe and York Urban, carefully
reannotate a subset of images and show that (i) existing detectors have
improved quality on updated annotations without retraining, suggesting that new
annotations correlate better with the notion of correct line segment detection;
(ii) the gap between accuracies of our detector and others diminishes to
negligible 0.2 Fh , with our method being the fastest.