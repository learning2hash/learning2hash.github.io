---
layout: publication
title: 'FSCE: Few-shot Object Detection Via Contrastive Proposal Encoding'
authors: Bo Sun, Banghuai Li, Shengcai Cai, Ye Yuan, Chi Zhang
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: sun2021fsce
citations: 353
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.05950'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Sun et al.
---
Emerging interests have been brought to recognize previously unseen objects
given very few training examples, known as few-shot object detection (FSOD).
Recent researches demonstrate that good feature embedding is the key to reach
favorable few-shot learning performance. We observe object proposals with
different Intersection-of-Union (IoU) scores are analogous to the intra-image
augmentation used in contrastive approaches. And we exploit this analogy and
incorporate supervised contrastive learning to achieve more robust objects
representations in FSOD. We present Few-Shot object detection via Contrastive
proposals Encoding (FSCE), a simple yet effective approach to learning
contrastive-aware object proposal encodings that facilitate the classification
of detected objects. We notice the degradation of average precision (AP) for
rare objects mainly comes from misclassifying novel instances as confusable
classes. And we ease the misclassification issues by promoting instance level
intra-class compactness and inter-class variance via our contrastive proposal
encoding loss (CPE loss). Our design outperforms current state-of-the-art works
in any shot and all data splits, with up to +8.8% on standard benchmark PASCAL
VOC and +2.7% on challenging COCO benchmark. Code is available at: https:
//github.com/MegviiDetection/FSCE