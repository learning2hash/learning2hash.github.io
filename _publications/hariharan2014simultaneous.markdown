---
layout: publication
title: Simultaneous Detection And Segmentation
authors: "Bharath Hariharan, Pablo Arbel\xE1ez, Ross Girshick, Jitendra Malik"
conference: Lecture Notes in Computer Science
year: 2014
bibkey: hariharan2014simultaneous
citations: 1110
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1407.1808'}]
tags: []
short_authors: Hariharan et al.
---
We aim to detect all instances of a category in an image and, for each
instance, mark the pixels that belong to it. We call this task Simultaneous
Detection and Segmentation (SDS). Unlike classical bounding box detection, SDS
requires a segmentation and not just a box. Unlike classical semantic
segmentation, we require individual object instances. We build on recent work
that uses convolutional neural networks to classify category-independent region
proposals (R-CNN [16]), introducing a novel architecture tailored for SDS. We
then use category-specific, top- down figure-ground predictions to refine our
bottom-up proposals. We show a 7 point boost (16% relative) over our baselines
on SDS, a 5 point boost (10% relative) over state-of-the-art on semantic
segmentation, and state-of-the-art performance in object detection. Finally, we
provide diagnostic tools that unpack performance and provide directions for
future work.