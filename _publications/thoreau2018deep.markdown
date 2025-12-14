---
layout: publication
title: Deep Similarity Metric Learning For Real-time Pedestrian Tracking
authors: Michael Thoreau, Navinda Kottege
conference: Arxiv
year: 2018
bibkey: thoreau2018deep
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.07592'}]
tags: [Evaluation, Distance Metric Learning, Datasets, Efficiency]
short_authors: Michael Thoreau, Navinda Kottege
---
Tracking by detection is a common approach to solving the Multiple Object
Tracking problem. In this paper we show how learning a deep similarity metric
can improve three key aspects of pedestrian tracking on a multiple object
tracking benchmark. We train a convolutional neural network to learn an
embedding function in a Siamese configuration on a large person
re-identification dataset. The offline-trained embedding network is integrated
in to the tracking formulation to improve performance while retaining real-time
performance. The proposed tracker stores appearance metrics while detections
are strong, using this appearance information to: prevent ID switches,
associate tracklets through occlusion, and propose new detections where
detector confidence is low. This method achieves competitive results in
evaluation, especially among online, real-time approaches. We present an
ablative study showing the impact of each of the three uses of our deep
appearance metric.