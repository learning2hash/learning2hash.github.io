---
layout: publication
title: 'Superpoint: Self-supervised Interest Point Detection And Description'
authors: Daniel Detone, Tomasz Malisiewicz, Andrew Rabinovich
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2018
bibkey: detone2017superpoint
citations: 2312
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.07629'}]
tags: ["CVPR", "Self-Supervised"]
short_authors: Daniel Detone, Tomasz Malisiewicz, Andrew Rabinovich
---
This paper presents a self-supervised framework for training interest point
detectors and descriptors suitable for a large number of multiple-view geometry
problems in computer vision. As opposed to patch-based neural networks, our
fully-convolutional model operates on full-sized images and jointly computes
pixel-level interest point locations and associated descriptors in one forward
pass. We introduce Homographic Adaptation, a multi-scale, multi-homography
approach for boosting interest point detection repeatability and performing
cross-domain adaptation (e.g., synthetic-to-real). Our model, when trained on
the MS-COCO generic image dataset using Homographic Adaptation, is able to
repeatedly detect a much richer set of interest points than the initial
pre-adapted deep model and any other traditional corner detector. The final
system gives rise to state-of-the-art homography estimation results on HPatches
when compared to LIFT, SIFT and ORB.