---
layout: publication
title: 'Location Field Descriptors: Single Image 3D Model Retrieval In The Wild'
authors: Alexander Grabner, Peter M. Roth, Vincent Lepetit
conference: 2019 International Conference on 3D Vision (3DV)
year: 2019
bibkey: grabner2019location
citations: 37
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.02853'}]
tags: ["Datasets", "Evaluation"]
short_authors: Alexander Grabner, Peter M. Roth, Vincent Lepetit
---
We present Location Field Descriptors, a novel approach for single image 3D
model retrieval in the wild. In contrast to previous methods that directly map
3D models and RGB images to an embedding space, we establish a common low-level
representation in the form of location fields from which we compute pose
invariant 3D shape descriptors. Location fields encode correspondences between
2D pixels and 3D surface coordinates and, thus, explicitly capture 3D shape and
3D pose information without appearance variations which are irrelevant for the
task. This early fusion of 3D models and RGB images results in three main
advantages: First, the bottleneck location field prediction acts as a
regularizer during training. Second, major parts of the system benefit from
training on a virtually infinite amount of synthetic data. Finally, the
predicted location fields are visually interpretable and unblackbox the system.
We evaluate our proposed approach on three challenging real-world datasets
(Pix3D, Comp, and Stanford) with different object categories and significantly
outperform the state-of-the-art by up to 20% absolute in multiple 3D retrieval
metrics.