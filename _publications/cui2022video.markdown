---
layout: publication
title: Video Moment Retrieval From Text Queries Via Single Frame Annotation
authors: Ran Cui, Tianwen Qian, Pai Peng, Elena Daskalaki, Jingjing Chen, Xiaowei
  Guo, Huyang Sun, Yu-Gang Jiang
conference: Proceedings of the 45th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2022
bibkey: cui2022video
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.09409'}]
tags: ["SIGIR"]
short_authors: Cui et al.
---
Video moment retrieval aims at finding the start and end timestamps of a
moment (part of a video) described by a given natural language query. Fully
supervised methods need complete temporal boundary annotations to achieve
promising results, which is costly since the annotator needs to watch the whole
moment. Weakly supervised methods only rely on the paired video and query, but
the performance is relatively poor. In this paper, we look closer into the
annotation process and propose a new paradigm called "glance annotation". This
paradigm requires the timestamp of only one single random frame, which we refer
to as a "glance", within the temporal boundary of the fully supervised
counterpart. We argue this is beneficial because comparing to weak supervision,
trivial cost is added yet more potential in performance is provided. Under the
glance annotation setting, we propose a method named as Video moment retrieval
via Glance Annotation (ViGA) based on contrastive learning. ViGA cuts the input
video into clips and contrasts between clips and queries, in which glance
guided Gaussian distributed weights are assigned to all clips. Our extensive
experiments indicate that ViGA achieves better results than the
state-of-the-art weakly supervised methods by a large margin, even comparable
to fully supervised methods in some cases.