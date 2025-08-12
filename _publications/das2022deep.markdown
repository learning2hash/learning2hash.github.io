---
layout: publication
title: Deep Multi-task Networks For Occluded Pedestrian Pose Estimation
authors: "Arindam Das, Sudip Das, Ganesh Sistu, Jonathan Horgan, Ujjwal Bhattacharya,\
  \ Edward Jones, Martin Glavin, Ciar\xE1n Eising"
conference: 24th Irish Machine Vision and Image Processing Conference
year: 2022
bibkey: das2022deep
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.07510'}]
tags: []
short_authors: Das et al.
---
Most of the existing works on pedestrian pose estimation do not consider
estimating the pose of an occluded pedestrian, as the annotations of the
occluded parts are not available in relevant automotive datasets. For example,
CityPersons, a well-known dataset for pedestrian detection in automotive scenes
does not provide pose annotations, whereas MS-COCO, a non-automotive dataset,
contains human pose estimation. In this work, we propose a multi-task framework
to extract pedestrian features through detection and instance segmentation
tasks performed separately on these two distributions. Thereafter, an encoder
learns pose specific features using an unsupervised instance-level domain
adaptation method for the pedestrian instances from both distributions. The
proposed framework has improved state-of-the-art performances of pose
estimation, pedestrian detection, and instance segmentation.