---
layout: publication
title: End-to-end Trainable Multi-instance Pose Estimation With Transformers
authors: Lucas Stoffl, Maxime Vidal, Alexander Mathis
conference: Arxiv
year: 2021
bibkey: stoffl2021end
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.12115'}]
tags: ["Transformer Based ANN"]
short_authors: Lucas Stoffl, Maxime Vidal, Alexander Mathis
---
We propose an end-to-end trainable approach for multi-instance pose
estimation, called POET (POse Estimation Transformer). Combining a
convolutional neural network with a transformer encoder-decoder architecture,
we formulate multiinstance pose estimation from images as a direct set
prediction problem. Our model is able to directly regress the pose of all
individuals, utilizing a bipartite matching scheme. POET is trained using a
novel set-based global loss that consists of a keypoint loss, a visibility loss
and a class loss. POET reasons about the relations between multiple detected
individuals and the full image context to directly predict their poses in
parallel. We show that POET achieves high accuracy on the COCO keypoint
detection task while having less parameters and higher inference speed than
other bottom-up and top-down approaches. Moreover, we show successful transfer
learning when applying POET to animal pose estimation. To the best of our
knowledge, this model is the first end-to-end trainable multi-instance pose
estimation method and we hope it will serve as a simple and promising
alternative.