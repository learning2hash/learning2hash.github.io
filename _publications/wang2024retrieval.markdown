---
layout: publication
title: Retrieval Augmented Image Harmonization
authors: Haolin Wang, Ming Liu, Zifei Yan, Chao Zhou, Longan Xiao, Wangmeng Zuo
conference: Arxiv
year: 2024
bibkey: wang2024retrieval
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.13916'}]
tags: [Evaluation, Tools & Libraries, Datasets, Similarity Search]
short_authors: Wang et al.
---
When embedding objects (foreground) into images (background), considering the
influence of photography conditions like illumination, it is usually necessary
to perform image harmonization to make the foreground object coordinate with
the background image in terms of brightness, color, and etc. Although existing
image harmonization methods have made continuous efforts toward visually
pleasing results, they are still plagued by two main issues. Firstly, the image
harmonization becomes highly ill-posed when there are no contents similar to
the foreground object in the background, making the harmonization results
unreliable. Secondly, even when similar contents are available, the
harmonization process is often interfered with by irrelevant areas, mainly
attributed to an insufficient understanding of image contents and inaccurate
attention. As a remedy, we present a retrieval-augmented image harmonization
(Raiha) framework, which seeks proper reference images to reduce the
ill-posedness and restricts the attention to better utilize the useful
information. Specifically, an efficient retrieval method is designed to find
reference images that contain similar objects as the foreground while the
illumination is consistent with the background. For training the Raiha
framework to effectively utilize the reference information, a data augmentation
strategy is delicately designed by leveraging existing non-reference image
harmonization datasets. Besides, the image content priors are introduced to
ensure reasonable attention. With the presented Raiha framework, the image
harmonization performance is greatly boosted under both non-reference and
retrieval-augmented settings. The source code and pre-trained models will be
publicly available.