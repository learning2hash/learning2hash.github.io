---
layout: publication
title: Attention-set Based Metric Learning For Video Face Recognition
authors: Yibo Hu, Xiang Wu, Ran He
conference: 2017 4th IAPR Asian Conference on Pattern Recognition (ACPR)
year: 2017
bibkey: hu2017attention
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.03805'}]
tags: ["Distance Metric Learning"]
short_authors: Yibo Hu, Xiang Wu, Ran He
---
Face recognition has made great progress with the development of deep
learning. However, video face recognition (VFR) is still an ongoing task due to
various illumination, low-resolution, pose variations and motion blur. Most
existing CNN-based VFR methods only obtain a feature vector from a single image
and simply aggregate the features in a video, which less consider the
correlations of face images in one video. In this paper, we propose a novel
Attention-Set based Metric Learning (ASML) method to measure the statistical
characteristics of image sets. It is a promising and generalized extension of
Maximum Mean Discrepancy with memory attention weighting. First, we define an
effective distance metric on image sets, which explicitly minimizes the
intra-set distance and maximizes the inter-set distance simultaneously. Second,
inspired by Neural Turing Machine, a Memory Attention Weighting is proposed to
adapt set-aware global contents. Then ASML is naturally integrated into CNNs,
resulting in an end-to-end learning scheme. Our method achieves
state-of-the-art performance for the task of video face recognition on the
three widely used benchmarks including YouTubeFace, YouTube Celebrities and
Celebrity-1000.