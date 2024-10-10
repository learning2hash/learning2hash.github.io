---
layout: publication
title: Encode The Unseen Predictive Video Hashing For Scalable Mid-stream Retrieval
authors: Yu Tong, Padoy Nicolas
conference: "Arxiv"
year: 2020
bibkey: yu2020encode
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2009.14661"}
tags: ['ARXIV', 'Video Retrieval']
---
This paper tackles a new problem in computer vision mid-stream video-to-video retrieval. This task which consists in searching a database for content similar to a video right as it is playing e.g. from a live stream exhibits challenging characteristics. Only the beginning part of the video is available as query and new frames are constantly added as the video plays out. To perform retrieval in this demanding situation we propose an approach based on a binary encoder that is both predictive and incremental in order to (1) account for the missing video content at query time and (2) keep up with repeated continuously evolving queries throughout the streaming. In particular we present the first hashing framework that infers the unseen future content of a currently playing video. Experiments on FCVID and ActivityNet demonstrate the feasibility of this task. Our approach also yields a significant mAP@20 performance increase compared to a baseline adapted from the literature for this task for instance 7.437; (2.637;) increase at 2037; (5037;) of elapsed runtime on FCVID using bitcodes of size 192 bits.
