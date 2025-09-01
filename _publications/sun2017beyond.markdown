---
layout: publication
title: 'Beyond Part Models: Person Retrieval With Refined Part Pooling (and A Strong
  Convolutional Baseline)'
authors: Yifan Sun, Liang Zheng, Yi Yang, Qi Tian, Shengjin Wang
conference: Lecture Notes in Computer Science
year: 2018
bibkey: sun2017beyond
citations: 2332
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.09349'}]
tags: ["Datasets", "Evaluation"]
short_authors: Sun et al.
---
Employing part-level features for pedestrian image description offers
fine-grained information and has been verified as beneficial for person
retrieval in very recent literature. A prerequisite of part discovery is that
each part should be well located. Instead of using external cues, e.g., pose
estimation, to directly locate parts, this paper lays emphasis on the content
consistency within each part.
  Specifically, we target at learning discriminative part-informed features for
person retrieval and make two contributions. (i) A network named Part-based
Convolutional Baseline (PCB). Given an image input, it outputs a convolutional
descriptor consisting of several part-level features. With a uniform partition
strategy, PCB achieves competitive results with the state-of-the-art methods,
proving itself as a strong convolutional baseline for person retrieval.
  (ii) A refined part pooling (RPP) method. Uniform partition inevitably incurs
outliers in each part, which are in fact more similar to other parts. RPP
re-assigns these outliers to the parts they are closest to, resulting in
refined parts with enhanced within-part consistency. Experiment confirms that
RPP allows PCB to gain another round of performance boost. For instance, on the
Market-1501 dataset, we achieve (77.4+4.2)% mAP and (92.3+1.5)% rank-1
accuracy, surpassing the state of the art by a large margin.