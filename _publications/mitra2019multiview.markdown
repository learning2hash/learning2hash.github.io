---
layout: publication
title: Multiview-consistent Semi-supervised Learning For 3D Human Pose Estimation
authors: Rahul Mitra, Nitesh B. Gundavarapu, Abhishek Sharma, Arjun Jain
conference: Arxiv
year: 2019
bibkey: mitra2019multiview
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.05293'}]
tags: ["Datasets", "Evaluation", "Supervised"]
short_authors: Mitra et al.
---
The best performing methods for 3D human pose estimation from monocular
images require large amounts of in-the-wild 2D and controlled 3D pose annotated
datasets which are costly and require sophisticated systems to acquire. To
reduce this annotation dependency, we propose Multiview-Consistent Semi
Supervised Learning (MCSS) framework that utilizes similarity in pose
information from unannotated, uncalibrated but synchronized multi-view videos
of human motions as additional weak supervision signal to guide 3D human pose
regression. Our framework applies hard-negative mining based on temporal
relations in multi-view videos to arrive at a multi-view consistent pose
embedding. When jointly trained with limited 3D pose annotations, our approach
improves the baseline by 25% and state-of-the-art by 8.7%, whilst using
substantially smaller networks. Lastly, but importantly, we demonstrate the
advantages of the learned embedding and establish view-invariant pose retrieval
benchmarks on two popular, publicly available multi-view human pose datasets,
Human 3.6M and MPI-INF-3DHP, to facilitate future research.