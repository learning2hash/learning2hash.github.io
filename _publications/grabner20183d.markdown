---
layout: publication
title: 3D Pose Estimation And 3D Model Retrieval For Objects In The Wild
authors: Alexander Grabner, Peter M. Roth, Vincent Lepetit
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: grabner20183d
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.11493'}]
tags: ["CVPR", "Distance Metric Learning", "Efficiency", "Image Retrieval", "Scalability"]
short_authors: Alexander Grabner, Peter M. Roth, Vincent Lepetit
---
We propose a scalable, efficient and accurate approach to retrieve 3D models
for objects in the wild. Our contribution is twofold. We first present a 3D
pose estimation approach for object categories which significantly outperforms
the state-of-the-art on Pascal3D+. Second, we use the estimated pose as a prior
to retrieve 3D models which accurately represent the geometry of objects in RGB
images. For this purpose, we render depth images from 3D models under our
predicted pose and match learned image descriptors of RGB images against those
of rendered depth images using a CNN-based multi-view metric learning approach.
In this way, we are the first to report quantitative results for 3D model
retrieval on Pascal3D+, where our method chooses the same models as human
annotators for 50% of the validation images on average. In addition, we show
that our method, which was trained purely on Pascal3D+, retrieves rich and
accurate 3D models from ShapeNet given RGB images of objects in the wild.