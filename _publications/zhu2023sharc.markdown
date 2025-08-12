---
layout: publication
title: 'Sharc: Shape And Appearance Recognition For Person Identification In-the-wild'
authors: Haidong Zhu, Wanrong Zheng, Zhaoheng Zheng, Ram Nevatia
conference: 2024 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2024
bibkey: zhu2023sharc
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.15946'}]
tags: []
short_authors: Zhu et al.
---
Identifying individuals in unconstrained video settings is a valuable yet
challenging task in biometric analysis due to variations in appearances,
environments, degradations, and occlusions. In this paper, we present ShARc, a
multimodal approach for video-based person identification in uncontrolled
environments that emphasizes 3-D body shape, pose, and appearance. We introduce
two encoders: a Pose and Shape Encoder (PSE) and an Aggregated Appearance
Encoder (AAE). PSE encodes the body shape via binarized silhouettes, skeleton
motions, and 3-D body shape, while AAE provides two levels of temporal
appearance feature aggregation: attention-based feature aggregation and
averaging aggregation. For attention-based feature aggregation, we employ
spatial and temporal attention to focus on key areas for person distinction.
For averaging aggregation, we introduce a novel flattening layer after
averaging to extract more distinguishable information and reduce overfitting of
attention. We utilize centroid feature averaging for gallery registration. We
demonstrate significant improvements over existing state-of-the-art methods on
public datasets, including CCVID, MEVID, and BRIAR.