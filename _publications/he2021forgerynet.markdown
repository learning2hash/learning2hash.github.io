---
layout: publication
title: 'Forgerynet: A Versatile Benchmark For Comprehensive Forgery Analysis'
authors: Yinan He, Bei Gan, Siyu Chen, Yichun Zhou, Guojun Yin, Luchuan Song, Lu Sheng,
  Jing Shao, Ziwei Liu
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: he2021forgerynet
citations: 84
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.05630'}]
tags: ["CVPR", "Datasets", "Evaluation"]
short_authors: He et al.
---
The rapid progress of photorealistic synthesis techniques has reached at a
critical point where the boundary between real and manipulated images starts to
blur. Thus, benchmarking and advancing digital forgery analysis have become a
pressing issue. However, existing face forgery datasets either have limited
diversity or only support coarse-grained analysis. To counter this emerging
threat, we construct the ForgeryNet dataset, an extremely large face forgery
dataset with unified annotations in image- and video-level data across four
tasks: 1) Image Forgery Classification, including two-way (real / fake),
three-way (real / fake with identity-replaced forgery approaches / fake with
identity-remained forgery approaches), and n-way (real and 15 respective
forgery approaches) classification. 2) Spatial Forgery Localization, which
segments the manipulated area of fake images compared to their corresponding
source real images. 3) Video Forgery Classification, which re-defines the
video-level forgery classification with manipulated frames in random positions.
This task is important because attackers in real world are free to manipulate
any target frame. and 4) Temporal Forgery Localization, to localize the
temporal segments which are manipulated. ForgeryNet is by far the largest
publicly available deep face forgery dataset in terms of data-scale (2.9
million images, 221,247 videos), manipulations (7 image-level approaches, 8
video-level approaches), perturbations (36 independent and more mixed
perturbations) and annotations (6.3 million classification labels, 2.9 million
manipulated area annotations and 221,247 temporal forgery segment labels). We
perform extensive benchmarking and studies of existing face forensics methods
and obtain several valuable observations.