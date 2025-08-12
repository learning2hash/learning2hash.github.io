---
layout: publication
title: 'Keypointnet: A Large-scale 3D Keypoint Dataset Aggregated From Numerous Human
  Annotations'
authors: Yang You, Yujing Lou, Chengkun Li, Zhoujun Cheng, Liangwei Li, Lizhuang Ma,
  Weiming Wang, Cewu Lu
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: you2020keypointnet
citations: 61
additional_links: [{name: Code, url: 'https://github.com/qq456cvb/KeypointNet'}, {
    name: Paper, url: 'https://arxiv.org/abs/2002.12687'}]
tags: ["CVPR", "Datasets"]
short_authors: You et al.
---
Detecting 3D objects keypoints is of great interest to the areas of both
graphics and computer vision. There have been several 2D and 3D keypoint
datasets aiming to address this problem in a data-driven way. These datasets,
however, either lack scalability or bring ambiguity to the definition of
keypoints. Therefore, we present KeypointNet: the first large-scale and diverse
3D keypoint dataset that contains 103,450 keypoints and 8,234 3D models from 16
object categories, by leveraging numerous human annotations. To handle the
inconsistency between annotations from different people, we propose a novel
method to aggregate these keypoints automatically, through minimization of a
fidelity loss. Finally, ten state-of-the-art methods are benchmarked on our
proposed dataset. Our code and data are available on
https://github.com/qq456cvb/KeypointNet.