---
layout: publication
title: 'Ndt-transformer: Large-scale 3D Point Cloud Localisation Using The Normal
  Distribution Transform Representation'
authors: Zhicheng Zhou, Cheng Zhao, Daniel Adolfsson, Songzhi Su, Yang Gao, Tom Duckett,
  Li Sun
conference: 2021 IEEE International Conference on Robotics and Automation (ICRA)
year: 2021
bibkey: zhou2021ndt
citations: 98
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.12292'}]
tags: ["Efficiency", "ICRA", "Scalability"]
short_authors: Zhou et al.
---
3D point cloud-based place recognition is highly demanded by autonomous
driving in GPS-challenged environments and serves as an essential component
(i.e. loop-closure detection) in lidar-based SLAM systems. This paper proposes
a novel approach, named NDT-Transformer, for realtime and large-scale place
recognition using 3D point clouds. Specifically, a 3D Normal Distribution
Transform (NDT) representation is employed to condense the raw, dense 3D point
cloud as probabilistic distributions (NDT cells) to provide the geometrical
shape description. Then a novel NDT-Transformer network learns a global
descriptor from a set of 3D NDT cell representations. Benefiting from the NDT
representation and NDT-Transformer network, the learned global descriptors are
enriched with both geometrical and contextual information. Finally, descriptor
retrieval is achieved using a query-database for place recognition. Compared to
the state-of-the-art methods, the proposed approach achieves an improvement of
7.52% on average top 1 recall and 2.73% on average top 1% recall on the Oxford
Robotcar benchmark.