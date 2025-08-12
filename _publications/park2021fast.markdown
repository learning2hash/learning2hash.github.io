---
layout: publication
title: Fast Point Transformer
authors: Chunghyun Park, Yoonwoo Jeong, Minsu Cho, Jaesik Park
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: park2021fast
citations: 131
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.04702'}]
tags: ["CVPR"]
short_authors: Park et al.
---
The recent success of neural networks enables a better interpretation of 3D
point clouds, but processing a large-scale 3D scene remains a challenging
problem. Most current approaches divide a large-scale scene into small regions
and combine the local predictions together. However, this scheme inevitably
involves additional stages for pre- and post-processing and may also degrade
the final output due to predictions in a local perspective. This paper
introduces Fast Point Transformer that consists of a new lightweight
self-attention layer. Our approach encodes continuous 3D coordinates, and the
voxel hashing-based architecture boosts computational efficiency. The proposed
method is demonstrated with 3D semantic segmentation and 3D detection. The
accuracy of our approach is competitive to the best voxel-based method, and our
network achieves 129 times faster inference time than the state-of-the-art,
Point Transformer, with a reasonable accuracy trade-off in 3D semantic
segmentation on S3DIS dataset.