---
layout: publication
title: Fusing Local Similarities For Retrieval-based 3D Orientation Estimation Of
  Unseen Objects
authors: Chen Zhao, Yinlin Hu, Mathieu Salzmann
conference: Lecture Notes in Computer Science
year: 2022
bibkey: zhao2022fusing
citations: 0
additional_links: [{name: Code, url: 'https://sailor-z.github.io/projects/Unseen_Object_Pose.html'},
  {name: Paper, url: 'https://arxiv.org/abs/2203.08472'}]
tags: ["Datasets", "Efficiency", "Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Chen Zhao, Yinlin Hu, Mathieu Salzmann
---
In this paper, we tackle the task of estimating the 3D orientation of
previously-unseen objects from monocular images. This task contrasts with the
one considered by most existing deep learning methods which typically assume
that the testing objects have been observed during training. To handle the
unseen objects, we follow a retrieval-based strategy and prevent the network
from learning object-specific features by computing multi-scale local
similarities between the query image and synthetically-generated reference
images. We then introduce an adaptive fusion module that robustly aggregates
the local similarities into a global similarity score of pairwise images.
Furthermore, we speed up the retrieval process by developing a fast retrieval
strategy. Our experiments on the LineMOD, LineMOD-Occluded, and T-LESS datasets
show that our method yields a significantly better generalization to unseen
objects than previous works. Our code and pre-trained models are available at
https://sailor-z.github.io/projects/Unseen_Object_Pose.html.