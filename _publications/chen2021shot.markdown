---
layout: publication
title: Shot Contrastive Self-supervised Learning For Scene Boundary Detection
authors: Shixing Chen, Xiaohan Nie, David Fan, Dongqing Zhang, Vimal Bhat, Raffay
  Hamid
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: chen2021shot
citations: 42
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.13537'}]
tags: ["CVPR", "Self-Supervised"]
short_authors: Chen et al.
---
Scenes play a crucial role in breaking the storyline of movies and TV
episodes into semantically cohesive parts. However, given their complex
temporal structure, finding scene boundaries can be a challenging task
requiring large amounts of labeled training data. To address this challenge, we
present a self-supervised shot contrastive learning approach (ShotCoL) to learn
a shot representation that maximizes the similarity between nearby shots
compared to randomly selected shots. We show how to apply our learned shot
representation for the task of scene boundary detection to offer
state-of-the-art performance on the MovieNet dataset while requiring only ~25%
of the training labels, using 9x fewer model parameters and offering 7x faster
runtime. To assess the effectiveness of ShotCoL on novel applications of scene
boundary detection, we take on the problem of finding timestamps in movies and
TV episodes where video-ads can be inserted while offering a minimally
disruptive viewing experience. To this end, we collected a new dataset called
AdCuepoints with 3,975 movies and TV episodes, 2.2 million shots and 19,119
minimally disruptive ad cue-point labels. We present a thorough empirical
analysis on this dataset demonstrating the effectiveness of ShotCoL for ad
cue-points detection.