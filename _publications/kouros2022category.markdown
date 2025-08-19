---
layout: publication
title: Category-level Pose Retrieval With Contrastive Features Learnt With Occlusion
  Augmentation
authors: "Georgios Kouros, Shubham Shrivastava, C\xE9dric Picron, Sushruth Nagesh,\
  \ Punarjay Chakravarty, Tinne Tuytelaars"
conference: Arxiv
year: 2022
bibkey: kouros2022category
citations: 1
additional_links: [{name: Code, url: 'https://github.com/gkouros/contrastive-pose-retrieval.'},
  {name: Paper, url: 'https://arxiv.org/abs/2208.06195'}]
tags: [Datasets, Efficiency, Image Retrieval, Distance Metric Learning, Robustness,
  Evaluation]
short_authors: Kouros et al.
---
Pose estimation is usually tackled as either a bin classification or a
regression problem. In both cases, the idea is to directly predict the pose of
an object. This is a non-trivial task due to appearance variations between
similar poses and similarities between dissimilar poses. Instead, we follow the
key idea that comparing two poses is easier than directly predicting one.
Render-and-compare approaches have been employed to that end, however, they
tend to be unstable, computationally expensive, and slow for real-time
applications. We propose doing category-level pose estimation by learning an
alignment metric in an embedding space using a contrastive loss with a dynamic
margin and a continuous pose-label space. For efficient inference, we use a
simple real-time image retrieval scheme with a pre-rendered and pre-embedded
reference set of renderings. To achieve robustness to real-world conditions, we
employ synthetic occlusions, bounding box perturbations, and appearance
augmentations. Our approach achieves state-of-the-art performance on PASCAL3D
and OccludedPASCAL3D and surpasses the competing methods on KITTI3D in a
cross-dataset evaluation setting. The code is currently available at
https://github.com/gkouros/contrastive-pose-retrieval.