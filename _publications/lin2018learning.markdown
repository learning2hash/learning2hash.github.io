---
layout: publication
title: Learning a Disentangled Embedding for Monocular 3D Shape Retrieval and Pose
  Estimation
authors: Lin Kyaw Zaw, Xu Weipeng, Sun Qianru, Theobalt Christian, Chua Tat-seng
conference: Arxiv
year: 2018
bibkey: lin2018learning
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.09899'}]
tags: ["Datasets", "Evaluation"]
short_authors: Lin et al.
---
We propose a novel approach to jointly perform 3D shape retrieval and pose
estimation from monocular images.In order to make the method robust to
real-world image variations, e.g. complex textures and backgrounds, we learn an
embedding space from 3D data that only includes the relevant information,
namely the shape and pose. Our approach explicitly disentangles a shape vector
and a pose vector, which alleviates both pose bias for 3D shape retrieval and
categorical bias for pose estimation. We then train a CNN to map the images to
this embedding space, and then retrieve the closest 3D shape from the database
and estimate the 6D pose of the object. Our method achieves 10.3 median error
for pose estimation and 0.592 top-1-accuracy for category agnostic 3D object
retrieval on the Pascal3D+ dataset, outperforming the previous state-of-the-art
methods on both tasks.