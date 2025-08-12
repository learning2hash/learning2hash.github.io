---
layout: publication
title: Non-parametric Spatially Constrained Local Prior For Scene Parsing On Real-world
  Data
authors: Ligang Zhang
conference: Engineering Applications of Artificial Intelligence
year: 2020
bibkey: zhang2020non
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.12874'}]
tags: ["Datasets", "Evaluation"]
short_authors: Ligang Zhang
---
Scene parsing aims to recognize the object category of every pixel in scene
images, and it plays a central role in image content understanding and computer
vision applications. However, accurate scene parsing from unconstrained
real-world data is still a challenging task. In this paper, we present the
non-parametric Spatially Constrained Local Prior (SCLP) for scene parsing on
realistic data. For a given query image, the non-parametric SCLP is learnt by
first retrieving a subset of most similar training images to the query image
and then collecting prior information about object co-occurrence statistics
between spatial image blocks and between adjacent superpixels from the
retrieved subset. The SCLP is powerful in capturing both long- and short-range
context about inter-object correlations in the query image and can be
effectively integrated with traditional visual features to refine the
classification results. Our experiments on the SIFT Flow and PASCAL-Context
benchmark datasets show that the non-parametric SCLP used in conjunction with
superpixel-level visual features achieves one of the top performance compared
with state-of-the-art approaches.