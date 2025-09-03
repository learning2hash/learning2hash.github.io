---
layout: publication
title: 'SOLAR: Second-order Loss And Attention For Image Retrieval'
authors: Tony Ng, Vassileios Balntas, Yurun Tian, Krystian Mikolajczyk
conference: Lecture Notes in Computer Science
year: 2020
bibkey: ng2020solar
citations: 99
additional_links: [{name: Code, url: 'http://github'}, {name: Paper, url: 'https://arxiv.org/abs/2001.08972'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Image Retrieval"]
short_authors: Ng et al.
---
Recent works in deep-learning have shown that second-order information is
beneficial in many computer-vision tasks. Second-order information can be
enforced both in the spatial context and the abstract feature dimensions. In
this work, we explore two second-order components. One is focused on
second-order spatial information to increase the performance of image
descriptors, both local and global. It is used to re-weight feature maps, and
thus emphasise salient image locations that are subsequently used for
description. The second component is concerned with a second-order similarity
(SOS) loss, that we extend to global descriptors for image retrieval, and is
used to enhance the triplet loss with hard-negative mining. We validate our
approach on two different tasks and datasets for image retrieval and image
matching. The results show that our two second-order components complement each
other, bringing significant performance improvements in both tasks and lead to
state-of-the-art results across the public benchmarks. Code available at:
http://github.com/tonyngjichun/SOLAR