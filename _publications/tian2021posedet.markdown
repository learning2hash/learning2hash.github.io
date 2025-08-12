---
layout: publication
title: 'Posedet: Fast Multi-person Pose Estimation Using Pose Embedding'
authors: Chenyu Tian, Ran Yu, Xinyuan Zhao, Weihao Xia, Haoqian Wang, Yujiu Yang
conference: 2021 16th IEEE International Conference on Automatic Face and Gesture
  Recognition (FG 2021)
year: 2021
bibkey: tian2021posedet
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.10466'}]
tags: []
short_authors: Tian et al.
---
Current methods of multi-person pose estimation typically treat the
localization and the association of body joints separately. It is convenient
but inefficient, leading to additional computation and a waste of time. This
paper, however, presents a novel framework PoseDet (Estimating Pose by
Detection) to localize and associate body joints simultaneously at higher
inference speed. Moreover, we propose the keypoint-aware pose embedding to
represent an object in terms of the locations of its keypoints. The proposed
pose embedding contains semantic and geometric information, allowing us to
access discriminative and informative features efficiently. It is utilized for
candidate classification and body joint localization in PoseDet, leading to
robust predictions of various poses. This simple framework achieves an
unprecedented speed and a competitive accuracy on the COCO benchmark compared
with state-of-the-art methods. Extensive experiments on the CrowdPose benchmark
show the robustness in the crowd scenes. Source code is available.