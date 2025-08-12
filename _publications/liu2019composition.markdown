---
layout: publication
title: Composition-aware Image Aesthetics Assessment
authors: Dong Liu, Rohit Puri, Nagendra Kamath, Subhabrata Bhattachary
conference: 2020 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2020
bibkey: liu2019composition
citations: 60
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.10801'}]
tags: ["Evaluation"]
short_authors: Liu et al.
---
Automatic image aesthetics assessment is important for a wide variety of
applications such as on-line photo suggestion, photo album management and image
retrieval. Previous methods have focused on mapping the holistic image content
to a high or low aesthetics rating. However, the composition information of an
image characterizes the harmony of its visual elements according to the
principles of art, and provides richer information for learning aesthetics. In
this work, we propose to model the image composition information as the mutual
dependency of its local regions, and design a novel architecture to leverage
such information to boost the performance of aesthetics assessment. To achieve
this, we densely partition an image into local regions and compute
aesthetics-preserving features over the regions to characterize the aesthetics
properties of image content. With the feature representation of local regions,
we build a region composition graph in which each node denotes one region and
any two nodes are connected by an edge weighted by the similarity of the region
features. We perform reasoning on this graph via graph convolution, in which
the activation of each node is determined by its highly correlated neighbors.
Our method naturally uncovers the mutual dependency of local regions in the
network training procedure, and achieves the state-of-the-art performance on
the benchmark visual aesthetics datasets.