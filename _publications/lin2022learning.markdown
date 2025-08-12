---
layout: publication
title: Learning Modal-invariant And Temporal-memory For Video-based Visible-infrared
  Person Re-identification
authors: Xinyu Lin, Jinxing Li, Zeyu Ma, Huafeng Li, Shuang Li, Kaixiong Xu, Guangming
  Lu, David Zhang
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: lin2022learning
citations: 53
additional_links: [{name: Code, url: 'https://github.com/VCMproject233/MITML'}, {
    name: Paper, url: 'https://arxiv.org/abs/2208.02450'}]
tags: ["CVPR", "Multimodal Retrieval"]
short_authors: Lin et al.
---
Thanks for the cross-modal retrieval techniques, visible-infrared (RGB-IR)
person re-identification (Re-ID) is achieved by projecting them into a common
space, allowing person Re-ID in 24-hour surveillance systems. However, with
respect to the probe-to-gallery, almost all existing RGB-IR based cross-modal
person Re-ID methods focus on image-to-image matching, while the video-to-video
matching which contains much richer spatial- and temporal-information remains
under-explored. In this paper, we primarily study the video-based cross-modal
person Re-ID method. To achieve this task, a video-based RGB-IR dataset is
constructed, in which 927 valid identities with 463,259 frames and 21,863
tracklets captured by 12 RGB/IR cameras are collected. Based on our constructed
dataset, we prove that with the increase of frames in a tracklet, the
performance does meet more enhancement, demonstrating the significance of
video-to-video matching in RGB-IR person Re-ID. Additionally, a novel method is
further proposed, which not only projects two modalities to a modal-invariant
subspace, but also extracts the temporal-memory for motion-invariant. Thanks to
these two strategies, much better results are achieved on our video-based
cross-modal person Re-ID. The code and dataset are released at:
https://github.com/VCMproject233/MITML.