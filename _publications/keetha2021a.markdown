---
layout: publication
title: A Hierarchical Dual Model Of Environment- And Place-specific Utility For Visual
  Place Recognition
authors: Nikhil Varma Keetha, Michael Milford, Sourav Garg
conference: IEEE Robotics and Automation Letters
year: 2021
bibkey: keetha2021a
citations: 3
additional_links: [{name: Code, url: 'https://github.com/Nik-V9/HEAPUtil'}, {name: Paper,
    url: 'https://arxiv.org/abs/2107.02440'}]
tags: ["Datasets", "Evaluation", "Self-Supervised", "Supervised", "Unsupervised"]
short_authors: Nikhil Varma Keetha, Michael Milford, Sourav Garg
---
Visual Place Recognition (VPR) approaches have typically attempted to match
places by identifying visual cues, image regions or landmarks that have high
``utility'' in identifying a specific place. But this concept of utility is not
singular - rather it can take a range of forms. In this paper, we present a
novel approach to deduce two key types of utility for VPR: the utility of
visual cues `specific' to an environment, and to a particular place. We employ
contrastive learning principles to estimate both the environment- and
place-specific utility of Vector of Locally Aggregated Descriptors (VLAD)
clusters in an unsupervised manner, which is then used to guide local feature
matching through keypoint selection. By combining these two utility measures,
our approach achieves state-of-the-art performance on three challenging
benchmark datasets, while simultaneously reducing the required storage and
compute time. We provide further analysis demonstrating that unsupervised
cluster selection results in semantically meaningful results, that finer
grained categorization often has higher utility for VPR than high level
semantic categorization (e.g. building, road), and characterise how these two
utility measures vary across different places and environments. Source code is
made publicly available at https://github.com/Nik-V9/HEAPUtil.