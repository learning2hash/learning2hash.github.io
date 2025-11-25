---
layout: publication
title: Siamese Instance Search For Tracking
authors: Ran Tao, Efstratios Gavves, Arnold W. M. Smeulders
conference: 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2016
bibkey: tao2016siamese
citations: 1140
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1605.05863'}]
tags: ["CVPR", "Evaluation", "Similarity Search", "Video Retrieval"]
short_authors: Ran Tao, Efstratios Gavves, Arnold W. M. Smeulders
---
In this paper we present a tracker, which is radically different from
state-of-the-art trackers: we apply no model updating, no occlusion detection,
no combination of trackers, no geometric matching, and still deliver
state-of-the-art tracking performance, as demonstrated on the popular online
tracking benchmark (OTB) and six very challenging YouTube videos. The presented
tracker simply matches the initial patch of the target in the first frame with
candidates in a new frame and returns the most similar patch by a learned
matching function. The strength of the matching function comes from being
extensively trained generically, i.e., without any data of the target, using a
Siamese deep neural network, which we design for tracking. Once learned, the
matching function is used as is, without any adapting, to track previously
unseen targets. It turns out that the learned matching function is so powerful
that a simple tracker built upon it, coined Siamese INstance search Tracker,
SINT, which only uses the original observation of the target from the first
frame, suffices to reach state-of-the-art performance. Further, we show the
proposed tracker even allows for target re-identification after the target was
absent for a complete video shot.