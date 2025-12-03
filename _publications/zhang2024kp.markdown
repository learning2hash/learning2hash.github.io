---
layout: publication
title: 'KP-RED: Exploiting Semantic Keypoints For Joint 3D Shape Retrieval And Deformation'
authors: Ruida Zhang, Chenyangguang Zhang, Yan di, Fabian Manhardt, Xingyu Liu, Federico
  Tombari, Xiangyang Ji
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: zhang2024kp
citations: 1
additional_links: [{name: Code, url: 'https://github.com/lolrudy/KP-RED'}, {name: Paper,
    url: 'https://arxiv.org/abs/2403.10099'}]
tags: ["CVPR", "Datasets", "Tools & Libraries"]
short_authors: Zhang et al.
---
In this paper, we present KP-RED, a unified KeyPoint-driven REtrieval and
Deformation framework that takes object scans as input and jointly retrieves
and deforms the most geometrically similar CAD models from a pre-processed
database to tightly match the target. Unlike existing dense matching based
methods that typically struggle with noisy partial scans, we propose to
leverage category-consistent sparse keypoints to naturally handle both full and
partial object scans. Specifically, we first employ a lightweight retrieval
module to establish a keypoint-based embedding space, measuring the similarity
among objects by dynamically aggregating deformation-aware local-global
features around extracted keypoints. Objects that are close in the embedding
space are considered similar in geometry. Then we introduce the neural
cage-based deformation module that estimates the influence vector of each
keypoint upon cage vertices inside its local support region to control the
deformation of the retrieved shape. Extensive experiments on the synthetic
dataset PartNet and the real-world dataset Scan2CAD demonstrate that KP-RED
surpasses existing state-of-the-art approaches by a large margin. Codes and
trained models are released on https://github.com/lolrudy/KP-RED.