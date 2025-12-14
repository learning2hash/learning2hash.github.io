---
layout: publication
title: Lidar Iris For Loop-closure Detection
authors: Ying Wang, Zezhou Sun, Cheng-Zhong Xu, Sanjay Sarma, Jian Yang, Hui Kong
conference: Arxiv
year: 2019
bibkey: wang2019lidar
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.03825'}]
tags: [Evaluation]
short_authors: Wang et al.
---
In this paper, a global descriptor for a LiDAR point cloud, called LiDAR
Iris, is proposed for fast and accurate loop-closure detection. A binary
signature image can be obtained for each point cloud after several LoG-Gabor
filtering and thresholding operations on the LiDAR-Iris image representation.
Given two point clouds, their similarities can be calculated as the Hamming
distance of two corresponding binary signature images extracted from the two
point clouds, respectively. Our LiDAR-Iris method can achieve a pose-invariant
loop-closure detection at a descriptor level with the Fourier transform of the
LiDAR-Iris representation if assuming a 3D (x,y,yaw) pose space, although our
method can generally be applied to a 6D pose space by re-aligning point clouds
with an additional IMU sensor. Experimental results on five road-scene
sequences demonstrate its excellent performance in loop-closure detection.