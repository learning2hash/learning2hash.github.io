---
layout: publication
title: 'Trivol: Point Cloud Rendering Via Triple Volumes'
authors: Tao Hu, Xiaogang Xu, Ruihang Chu, Jiaya Jia
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: hu2023trivol
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.16485'}]
tags: ["CVPR"]
short_authors: Hu et al.
---
Existing learning-based methods for point cloud rendering adopt various 3D
representations and feature querying mechanisms to alleviate the sparsity
problem of point clouds. However, artifacts still appear in rendered images,
due to the challenges in extracting continuous and discriminative 3D features
from point clouds. In this paper, we present a dense while lightweight 3D
representation, named TriVol, that can be combined with NeRF to render
photo-realistic images from point clouds. Our TriVol consists of triple slim
volumes, each of which is encoded from the point cloud. TriVol has two
advantages. First, it fuses respective fields at different scales and thus
extracts local and non-local features for discriminative representation.
Second, since the volume size is greatly reduced, our 3D decoder can be
efficiently inferred, allowing us to increase the resolution of the 3D space to
render more point details. Extensive experiments on different benchmarks with
varying kinds of scenes/objects demonstrate our framework's effectiveness
compared with current approaches. Moreover, our framework has excellent
generalization ability to render a category of scenes/objects without
fine-tuning.