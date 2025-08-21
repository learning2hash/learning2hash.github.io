---
layout: publication
title: Person Re-identification With Fusion Of Hand-crafted And Deep Pose-based Body
  Region Features
authors: Jubin Johnson, Shunsuke Yasugi, Yoichi Sugino, Sugiri Pranata, Shengmei Shen
conference: Arxiv
year: 2018
bibkey: johnson2018person
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.10630'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Scalability"]
short_authors: Johnson et al.
---
Person re-identification (re-ID) aims to accurately re- trieve a person from
a large-scale database of images cap- tured across multiple cameras. Existing
works learn deep representations using a large training subset of unique per-
sons. However, identifying unseen persons is critical for a good re-ID
algorithm. Moreover, the misalignment be- tween person crops to detection
errors or pose variations leads to poor feature matching. In this work, we
present a fusion of handcrafted features and deep feature representa- tion
learned using multiple body parts to complement the global body features that
achieves high performance on un- seen test images. Pose information is used to
detect body regions that are passed through Convolutional Neural Net- works
(CNN) to guide feature learning. Finally, a metric learning step enables robust
distance matching on a dis- criminative subspace. Experimental results on 4
popular re-ID benchmark datasets namely VIPer, DukeMTMC-reID, Market-1501 and
CUHK03 show that the proposed method achieves state-of-the-art performance in
image-based per- son re-identification.