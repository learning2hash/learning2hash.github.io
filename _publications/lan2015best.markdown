---
layout: publication
title: 'The Best Of Both Worlds: Combining Data-independent And Data-driven Approaches
  For Action Recognition'
authors: Zhenzhong Lan, Dezhong Yao, Ming Lin, Shoou-I Yu, Alexander Hauptmann
conference: Arxiv
year: 2015
bibkey: lan2015best
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1505.04427'}]
tags: []
short_authors: Lan et al.
---
Motivated by the success of data-driven convolutional neural networks (CNNs)
in object recognition on static images, researchers are working hard towards
developing CNN equivalents for learning video features. However, learning video
features globally has proven to be quite a challenge due to its high
dimensionality, the lack of labelled data and the difficulty in processing
large-scale video data. Therefore, we propose to leverage effective techniques
from both data-driven and data-independent approaches to improve action
recognition system.
  Our contribution is three-fold. First, we propose a two-stream Stacked
Convolutional Independent Subspace Analysis (ConvISA) architecture to show that
unsupervised learning methods can significantly boost the performance of
traditional local features extracted from data-independent models. Second, we
demonstrate that by learning on video volumes detected by Improved Dense
Trajectory (IDT), we can seamlessly combine our novel local descriptors with
hand-crafted descriptors. Thus we can utilize available feature enhancing
techniques developed for hand-crafted descriptors. Finally, similar to
multi-class classification framework in CNNs, we propose a training-free
re-ranking technique that exploits the relationship among action classes to
improve the overall performance. Our experimental results on four benchmark
action recognition datasets show significantly improved performance.