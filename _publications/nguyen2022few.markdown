---
layout: publication
title: Few-shot Object Counting And Detection
authors: Thanh Nguyen, Chau Pham, Khoi Nguyen, Minh Hoai
conference: Lecture Notes in Computer Science
year: 2022
bibkey: nguyen2022few
citations: 28
additional_links: [{name: Code, url: 'https://github.com/VinAIResearch/Counting-DETR'},
  {name: Paper, url: 'https://arxiv.org/abs/2207.10988'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Nguyen et al.
---
We tackle a new task of few-shot object counting and detection. Given a few
exemplar bounding boxes of a target object class, we seek to count and detect
all objects of the target class. This task shares the same supervision as the
few-shot object counting but additionally outputs the object bounding boxes
along with the total object count. To address this challenging problem, we
introduce a novel two-stage training strategy and a novel uncertainty-aware
few-shot object detector: Counting-DETR. The former is aimed at generating
pseudo ground-truth bounding boxes to train the latter. The latter leverages
the pseudo ground-truth provided by the former but takes the necessary steps to
account for the imperfection of pseudo ground-truth. To validate the
performance of our method on the new task, we introduce two new datasets named
FSCD-147 and FSCD-LVIS. Both datasets contain images with complex scenes,
multiple object classes per image, and a huge variation in object shapes,
sizes, and appearance. Our proposed approach outperforms very strong baselines
adapted from few-shot object counting and few-shot object detection with a
large margin in both counting and detection metrics. The code and models are
available at https://github.com/VinAIResearch/Counting-DETR.