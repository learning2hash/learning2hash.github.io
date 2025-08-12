---
layout: publication
title: Learning Inclusion Matching For Animation Paint Bucket Colorization
authors: Yuekun Dai, Shangchen Zhou, Qinyue Li, Chongyi Li, Chen Change Loy
conference: Arxiv
year: 2024
bibkey: dai2024learning
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.18342'}]
tags: []
short_authors: Dai et al.
---
Colorizing line art is a pivotal task in the production of hand-drawn cel
animation. This typically involves digital painters using a paint bucket tool
to manually color each segment enclosed by lines, based on RGB values
predetermined by a color designer. This frame-by-frame process is both arduous
and time-intensive. Current automated methods mainly focus on segment matching.
This technique migrates colors from a reference to the target frame by aligning
features within line-enclosed segments across frames. However, issues like
occlusion and wrinkles in animations often disrupt these direct
correspondences, leading to mismatches. In this work, we introduce a new
learning-based inclusion matching pipeline, which directs the network to
comprehend the inclusion relationships between segments rather than relying
solely on direct visual correspondences. Our method features a two-stage
pipeline that integrates a coarse color warping module with an inclusion
matching module, enabling more nuanced and accurate colorization. To facilitate
the training of our network, we also develope a unique dataset, referred to as
PaintBucket-Character. This dataset includes rendered line arts alongside their
colorized counterparts, featuring various 3D characters. Extensive experiments
demonstrate the effectiveness and superiority of our method over existing
techniques.