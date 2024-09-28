---
layout: publication
title: GPU Accelerated Cascade Hashing Image Matching for Large Scale 3D Reconstruction
authors: Xu Tao, Sun Kun, Tao Wenbing
conference: "Arxiv"
year: 2018
bibkey: xu2018gpu
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1805.08995"}
tags: ['ARXIV', 'Graph']
---
Image feature point matching is a key step in Structure from Motion(SFM). However it is becoming more and more time consuming because the number of images is getting larger and larger. In this paper we proposed a GPU accelerated image matching method with improved Cascade Hashing. Firstly we propose a Disk-Memory-GPU data exchange strategy and optimize the load order of data so that the proposed method can deal with big data. Next we parallelize the Cascade Hashing method on GPU. An improved parallel reduction and an improved parallel hashing ranking are proposed to fulfill this task. Finally extensive experiments show that our image matching is about 20 times faster than SiftGPU on the same graphics card nearly 100 times faster than the CPU CasHash method and hundreds of times faster than the CPU Kd-Tree based matching method. Further more we introduce the epipolar constraint to the proposed method and use the epipolar geometry to guide the feature matching procedure which further reduces the matching cost.
