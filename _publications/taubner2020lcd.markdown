---
layout: publication
title: LCD -- Line Clustering And Description For Place Recognition
authors: Felix Taubner, Florian Tschopp, Tonci Novkovic, Roland Siegwart, Fadri Furrer
conference: 2020 International Conference on 3D Vision (3DV)
year: 2020
bibkey: taubner2020lcd
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.10867'}]
tags: ["Datasets", "Distance Metric Learning"]
short_authors: Taubner et al.
---
Current research on visual place recognition mostly focuses on aggregating
local visual features of an image into a single vector representation.
Therefore, high-level information such as the geometric arrangement of the
features is typically lost. In this paper, we introduce a novel learning-based
approach to place recognition, using RGB-D cameras and line clusters as visual
and geometric features. We state the place recognition problem as a problem of
recognizing clusters of lines instead of individual patches, thus maintaining
structural information. In our work, line clusters are defined as lines that
make up individual objects, hence our place recognition approach can be
understood as object recognition. 3D line segments are detected in RGB-D images
using state-of-the-art techniques. We present a neural network architecture
based on the attention mechanism for frame-wise line clustering. A similar
neural network is used for the description of these clusters with a compact
embedding of 128 floating point numbers, trained with triplet loss on training
data obtained from the InteriorNet dataset. We show experiments on a large
number of indoor scenes and compare our method with the bag-of-words
image-retrieval approach using SIFT and SuperPoint features and the global
descriptor NetVLAD. Trained only on synthetic data, our approach generalizes
well to real-world data captured with Kinect sensors, while also providing
information about the geometric arrangement of instances.