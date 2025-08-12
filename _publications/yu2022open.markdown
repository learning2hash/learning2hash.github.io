---
layout: publication
title: Open-world Object Detection Via Discriminative Class Prototype Learning
authors: Jinan Yu, Liyan Ma, Zhenglin Li, Yan Peng, Shaorong Xie
conference: 2022 IEEE International Conference on Image Processing (ICIP)
year: 2022
bibkey: yu2022open
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.11757'}]
tags: ["Evaluation"]
short_authors: Yu et al.
---
Open-world object detection (OWOD) is a challenging problem that combines
object detection with incremental learning and open-set learning. Compared to
standard object detection, the OWOD setting is task to: 1) detect objects seen
during training while identifying unseen classes, and 2) incrementally learn
the knowledge of the identified unknown objects when the corresponding
annotations is available. We propose a novel and efficient OWOD solution from a
prototype perspective, which we call OCPL: Open-world object detection via
discriminative Class Prototype Learning, which consists of a Proposal Embedding
Aggregator (PEA), an Embedding Space Compressor (ESC) and a Cosine
Similarity-based Classifier (CSC). All our proposed modules aim to learn the
discriminative embeddings of known classes in the feature space to minimize the
overlapping distributions of known and unknown classes, which is beneficial to
differentiate known and unknown classes. Extensive experiments performed on
PASCAL VOC and MS-COCO benchmark demonstrate the effectiveness of our proposed
method.