---
layout: publication
title: Weakly Supervised Video Moment Retrieval From Text Queries
authors: Niluthpol Chowdhury Mithun, Sujoy Paul, Amit K. Roy-Chowdhury
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: mithun2019weakly
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.03282'}]
tags: [Evaluation, Supervised, Datasets, CVPR, Tools & Libraries]
short_authors: Niluthpol Chowdhury Mithun, Sujoy Paul, Amit K. Roy-Chowdhury
---
There have been a few recent methods proposed in text to video moment
retrieval using natural language queries, but requiring full supervision during
training. However, acquiring a large number of training videos with temporal
boundary annotations for each text description is extremely time-consuming and
often not scalable. In order to cope with this issue, in this work, we
introduce the problem of learning from weak labels for the task of text to
video moment retrieval. The weak nature of the supervision is because, during
training, we only have access to the video-text pairs rather than the temporal
extent of the video to which different text descriptions relate. We propose a
joint visual-semantic embedding based framework that learns the notion of
relevant segments from video using only video-level sentence descriptions.
Specifically, our main idea is to utilize latent alignment between video frames
and sentence descriptions using Text-Guided Attention (TGA). TGA is then used
during the test phase to retrieve relevant moments. Experiments on two
benchmark datasets demonstrate that our method achieves comparable performance
to state-of-the-art fully supervised approaches.