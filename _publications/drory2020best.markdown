---
layout: publication
title: Best Buddies Registration For Point Clouds
authors: Amnon Drory, Tal Shomer, Shai Avidan, Raja Giryes
conference: Lecture Notes in Computer Science
year: 2020
bibkey: drory2020best
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.01912'}]
tags: ["Datasets", "Robustness"]
short_authors: Drory et al.
---
We propose new, and robust, loss functions for the point cloud registration
problem. Our loss functions are inspired by the Best Buddies Similarity (BBS)
measure that counts the number of mutual nearest neighbors between two point
sets. This measure has been shown to be robust to outliers and missing data in
the case of template matching for images. We present several algorithms,
collectively named Best Buddy Registration (BBR), where each algorithm consists
of optimizing one of these loss functions with Adam gradient descent. The loss
functions differ in several ways, including the distance function used
(point-to-point vs. point-to-plane), and how the BBS measure is combined with
the actual distances between pairs of points. Experiments on various data sets,
both synthetic and real, demonstrate the effectiveness of the BBR algorithms,
showing that they are quite robust to noise, outliers, and distractors, and
cope well with extremely sparse point clouds. One variant, BBR-F, achieves
state-of-the-art accuracy in the registration of automotive lidar scans taken
up to several seconds apart, from the KITTI and Apollo-Southbay datasets.