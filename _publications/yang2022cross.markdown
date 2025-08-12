---
layout: publication
title: Cross-image Relational Knowledge Distillation For Semantic Segmentation
authors: Chuanguang Yang, Helong Zhou, Zhulin An, Xue Jiang, Yongjun Xu, Qian Zhang
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: yang2022cross
citations: 149
additional_links: [{name: Code, url: 'https://github.com/winycg/CIRKD'}, {name: Paper,
    url: 'https://arxiv.org/abs/2204.06986'}]
tags: ["CVPR"]
short_authors: Yang et al.
---
Current Knowledge Distillation (KD) methods for semantic segmentation often
guide the student to mimic the teacher's structured information generated from
individual data samples. However, they ignore the global semantic relations
among pixels across various images that are valuable for KD. This paper
proposes a novel Cross-Image Relational KD (CIRKD), which focuses on
transferring structured pixel-to-pixel and pixel-to-region relations among the
whole images. The motivation is that a good teacher network could construct a
well-structured feature space in terms of global pixel dependencies. CIRKD
makes the student mimic better structured semantic relations from the teacher,
thus improving the segmentation performance. Experimental results over
Cityscapes, CamVid and Pascal VOC datasets demonstrate the effectiveness of our
proposed approach against state-of-the-art distillation methods. The code is
available at https://github.com/winycg/CIRKD.