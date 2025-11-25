---
layout: publication
title: Learning Test-time Augmentation For Content-based Image Retrieval
authors: Osman Tursun, Simon Denman, Sridha Sridharan, Clinton Fookes
conference: Computer Vision and Image Understanding
year: 2020
bibkey: tursun2020learning
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.01642'}]
tags: ["Datasets", "Distance Metric Learning", "Image Retrieval"]
short_authors: Tursun et al.
---
Off-the-shelf convolutional neural network features achieve outstanding
results in many image retrieval tasks. However, their invariance to target data
is pre-defined by the network architecture and training data. Existing image
retrieval approaches require fine-tuning or modification of pre-trained
networks to adapt to variations unique to the target data. In contrast, our
method enhances the invariance of off-the-shelf features by aggregating
features extracted from images augmented at test-time, with augmentations
guided by a policy learned through reinforcement learning. The learned policy
assigns different magnitudes and weights to the selected transformations, which
are selected from a list of image transformations. Policies are evaluated using
a metric learning protocol to learn the optimal policy. The model converges
quickly and the cost of each policy iteration is minimal as we propose an
off-line caching technique to greatly reduce the computational cost of
extracting features from augmented images. Experimental results on large
trademark retrieval (METU trademark dataset) and landmark retrieval (ROxford5k
and RParis6k scene datasets) tasks show that the learned ensemble of
transformations is highly effective for improving performance, and is
practical, and transferable.