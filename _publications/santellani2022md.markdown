---
layout: publication
title: 'Md-net: Multi-detector For Local Feature Extraction'
authors: Emanuele Santellani, Christian Sormann, Mattia Rossi, Andreas Kuhn, Friedrich
  Fraundorfer
conference: 2022 26th International Conference on Pattern Recognition (ICPR)
year: 2022
bibkey: santellani2022md
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.05350'}]
tags: ["Unsupervised"]
short_authors: Santellani et al.
---
Establishing a sparse set of keypoint correspon dences between images is a
fundamental task in many computer vision pipelines. Often, this translates into
a computationally expensive nearest neighbor search, where every keypoint
descriptor at one image must be compared with all the descriptors at the
others. In order to lower the computational cost of the matching phase, we
propose a deep feature extraction network capable of detecting a predefined
number of complementary sets of keypoints at each image. Since only the
descriptors within the same set need to be compared across the different
images, the matching phase computational complexity decreases with the number
of sets. We train our network to predict the keypoints and compute the
corresponding descriptors jointly. In particular, in order to learn
complementary sets of keypoints, we introduce a novel unsupervised loss which
penalizes intersections among the different sets. Additionally, we propose a
novel descriptor-based weighting scheme meant to penalize the detection of
keypoints with non-discriminative descriptors. With extensive experiments we
show that our feature extraction network, trained only on synthetically warped
images and in a fully unsupervised manner, achieves competitive results on 3D
reconstruction and re-localization tasks at a reduced matching complexity.