---
layout: publication
title: 'Secondpose: Se(3)-consistent Dual-stream Feature Fusion For Category-level
  Pose Estimation'
authors: Yamei Chen, Yan di, Guangyao Zhai, Fabian Manhardt, Chenyangguang Zhang,
  Ruida Zhang, Federico Tombari, Nassir Navab, Benjamin Busam
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: chen2023secondpose
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.11125'}]
tags: ["CVPR"]
short_authors: Chen et al.
---
Category-level object pose estimation, aiming to predict the 6D pose and 3D
size of objects from known categories, typically struggles with large
intra-class shape variation. Existing works utilizing mean shapes often fall
short of capturing this variation. To address this issue, we present
SecondPose, a novel approach integrating object-specific geometric features
with semantic category priors from DINOv2. Leveraging the advantage of DINOv2
in providing SE(3)-consistent semantic features, we hierarchically extract two
types of SE(3)-invariant geometric features to further encapsulate
local-to-global object-specific information. These geometric features are then
point-aligned with DINOv2 features to establish a consistent object
representation under SE(3) transformations, facilitating the mapping from
camera space to the pre-defined canonical space, thus further enhancing pose
estimation. Extensive experiments on NOCS-REAL275 demonstrate that SecondPose
achieves a 12.4% leap forward over the state-of-the-art. Moreover, on a more
complex dataset HouseCat6D which provides photometrically challenging objects,
SecondPose still surpasses other competitors by a large margin.