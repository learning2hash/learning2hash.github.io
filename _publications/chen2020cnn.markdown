---
layout: publication
title: A CNN Framenwork Based On Line Annotations For Detecting Nematodes In Microscopic
  Images
authors: "Long Chen, Martin Strauch, Matthias Daub, Xiaochen Jiang, Marcus Jansen,\
  \ Hans-Georg Luigs, Susanne Schultz-Kuhlmann, Stefan Kr\xFCssel, Dorif Merhof"
conference: Arxiv
year: 2020
bibkey: chen2020cnn
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.09795'}]
tags: []
short_authors: Chen et al.
---
Plant parasitic nematodes cause damage to crop plants on a global scale.
Robust detection on image data is a prerequisite for monitoring such nematodes,
as well as for many biological studies involving the nematode C. elegans, a
common model organism. Here, we propose a framework for detecting worm-shaped
objects in microscopic images that is based on convolutional neural networks
(CNNs). We annotate nematodes with curved lines along the body, which is more
suitable for worm-shaped objects than bounding boxes. The trained model
predicts worm skeletons and body endpoints. The endpoints serve to untangle the
skeletons from which segmentation masks are reconstructed by estimating the
body width at each location along the skeleton. With light-weight backbone
networks, we achieve 75.85 % precision, 73.02 % recall on a potato cyst
nematode data set and 84.20 % precision, 85.63 % recall on a public C. elegans
data set.