---
layout: publication
title: 'ELSD: Efficient Line Segment Detector And Descriptor'
authors: Haotian Zhang, Yicheng Luo, Fangbo Qin, Yijia He, Xiao Liu
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: zhang2021elsd
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.14205'}]
tags: ["Efficiency", "ICCV"]
short_authors: Zhang et al.
---
We present the novel Efficient Line Segment Detector and Descriptor (ELSD) to
simultaneously detect line segments and extract their descriptors in an image.
Unlike the traditional pipelines that conduct detection and description
separately, ELSD utilizes a shared feature extractor for both detection and
description, to provide the essential line features to the higher-level tasks
like SLAM and image matching in real time. First, we design the one-stage
compact model, and propose to use the mid-point, angle and length as the
minimal representation of line segment, which also guarantees the
center-symmetry. The non-centerness suppression is proposed to filter out the
fragmented line segments caused by lines' intersections. The fine offset
prediction is designed to refine the mid-point localization. Second, the line
descriptor branch is integrated with the detector branch, and the two branches
are jointly trained in an end-to-end manner. In the experiments, the proposed
ELSD achieves the state-of-the-art performance on the Wireframe dataset and
YorkUrban dataset, in both accuracy and efficiency. The line description
ability of ELSD also outperforms the previous works on the line matching task.