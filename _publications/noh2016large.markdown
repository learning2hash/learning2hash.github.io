---
layout: publication
title: Large-scale Image Retrieval With Attentive Deep Local Features
authors: Hyeonwoo Noh, Andre Araujo, Jack Sim, Tobias Weyand, Bohyung Han
conference: 2017 IEEE International Conference on Computer Vision (ICCV)
year: 2017
bibkey: noh2016large
citations: 812
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.06321'}]
tags: [ICCV, Scalability, Datasets, Image Retrieval, Tools & Libraries]
short_authors: Noh et al.
---
We propose an attentive local feature descriptor suitable for large-scale
image retrieval, referred to as DELF (DEep Local Feature). The new feature is
based on convolutional neural networks, which are trained only with image-level
annotations on a landmark image dataset. To identify semantically useful local
features for image retrieval, we also propose an attention mechanism for
keypoint selection, which shares most network layers with the descriptor. This
framework can be used for image retrieval as a drop-in replacement for other
keypoint detectors and descriptors, enabling more accurate feature matching and
geometric verification. Our system produces reliable confidence scores to
reject false positives---in particular, it is robust against queries that have
no correct match in the database. To evaluate the proposed descriptor, we
introduce a new large-scale dataset, referred to as Google-Landmarks dataset,
which involves challenges in both database and query such as background
clutter, partial occlusion, multiple landmarks, objects in variable scales,
etc. We show that DELF outperforms the state-of-the-art global and local
descriptors in the large-scale setting by significant margins. Code and dataset
can be found at the project webpage:
https://github.com/tensorflow/models/tree/master/research/delf .