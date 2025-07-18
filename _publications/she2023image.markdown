---
layout: publication
title: Image Patch-matching With Graph-based Learning In Street Scenes
authors: She et al.
conference: IEEE Transactions on Image Processing
year: 2023
bibkey: she2023image
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.04617'}]
tags: [DATASETS, Tools & Libraries, Graph Based ANN, Distance Metric Learning]
---
Matching landmark patches from a real-time image captured by an on-vehicle
camera with landmark patches in an image database plays an important role in
various computer perception tasks for autonomous driving. Current methods focus
on local matching for regions of interest and do not take into account spatial
neighborhood relationships among the image patches, which typically correspond
to objects in the environment. In this paper, we construct a spatial graph with
the graph vertices corresponding to patches and edges capturing the spatial
neighborhood information. We propose a joint feature and metric learning model
with graph-based learning. We provide a theoretical basis for the graph-based
loss by showing that the information distance between the distributions
conditioned on matched and unmatched pairs is maximized under our framework. We
evaluate our model using several street-scene datasets and demonstrate that our
approach achieves state-of-the-art matching results.