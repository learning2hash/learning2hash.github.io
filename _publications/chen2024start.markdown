---
layout: publication
title: 'Start From Video-music Retrieval: An Inter-intra Modal Loss For Cross Modal
  Retrieval'
authors: Zeyu Chen, Pengfei Zhang, Kai Ye, Wei Dong, Xin Feng, Yana Zhang
conference: Arxiv
year: 2024
bibkey: chen2024start
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.19415'}]
tags: ["Multimodal Retrieval", "Self-Supervised"]
short_authors: Chen et al.
---
The burgeoning short video industry has accelerated the advancement of
video-music retrieval technology, assisting content creators in selecting
appropriate music for their videos. In self-supervised training for
video-to-music retrieval, the video and music samples in the dataset are
separated from the same video work, so they are all one-to-one matches. This
does not match the real situation. In reality, a video can use different music
as background music, and a music can be used as background music for different
videos. Many videos and music that are not in a pair may be compatible, leading
to false negative noise in the dataset. A novel inter-intra modal (II) loss is
proposed as a solution. By reducing the variation of feature distribution
within the two modalities before and after the encoder, II loss can reduce the
model's overfitting to such noise without removing it in a costly and laborious
way. The video-music retrieval framework, II-CLVM (Contrastive Learning for
Video-Music Retrieval), incorporating the II Loss, achieves state-of-the-art
performance on the YouTube8M dataset. The framework II-CLVTM shows better
performance when retrieving music using multi-modal video information (such as
text in videos). Experiments are designed to show that II loss can effectively
alleviate the problem of false negative noise in retrieval tasks. Experiments
also show that II loss improves various self-supervised and supervised
uni-modal and cross-modal retrieval tasks, and can obtain good retrieval models
with a small amount of training samples.