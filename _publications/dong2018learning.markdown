---
layout: publication
title: Learning To Align Images Using Weak Geometric Supervision
authors: Jing Dong, Byron Boots, Frank Dellaert, Ranveer Chandra, Sudipta N. Sinha
conference: 2018 International Conference on 3D Vision (3DV)
year: 2018
bibkey: dong2018learning
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.01424'}]
tags: []
short_authors: Dong et al.
---
Image alignment tasks require accurate pixel correspondences, which are
usually recovered by matching local feature descriptors. Such descriptors are
often derived using supervised learning on existing datasets with ground truth
correspondences. However, the cost of creating such datasets is usually
prohibitive. In this paper, we propose a new approach to align two images
related by an unknown 2D homography where the local descriptor is learned from
scratch from the images and the homography is estimated simultaneously. Our key
insight is that a siamese convolutional neural network can be trained jointly
while iteratively updating the homography parameters by optimizing a single
loss function. Our method is currently weakly supervised because the input
images need to be roughly aligned.
  We have used this method to align images of different modalities such as RGB
and near-infra-red (NIR) without using any prior labeled data. Images
automatically aligned by our method were then used to train descriptors that
generalize to new images. We also evaluated our method on RGB images. On the
HPatches benchmark, our method achieves comparable accuracy to deep local
descriptors that were trained offline in a supervised setting.