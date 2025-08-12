---
layout: publication
title: 'Occluded Video Instance Segmentation: A Benchmark'
authors: Jiyang Qi, Yan Gao, Yao Hu, Xinggang Wang, Xiaoyu Liu, Xiang Bai, Serge Belongie,
  Alan Yuille, Philip H. S. Torr, Song Bai
conference: International Journal of Computer Vision
year: 2022
bibkey: qi2021occluded
citations: 70
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.01558'}]
tags: ["Datasets", "Evaluation"]
short_authors: Qi et al.
---
Can our video understanding systems perceive objects when a heavy occlusion
exists in a scene?
  To answer this question, we collect a large-scale dataset called OVIS for
occluded video instance segmentation, that is, to simultaneously detect,
segment, and track instances in occluded scenes. OVIS consists of 296k
high-quality instance masks from 25 semantic categories, where object
occlusions usually occur. While our human vision systems can understand those
occluded instances by contextual reasoning and association, our experiments
suggest that current video understanding systems cannot. On the OVIS dataset,
the highest AP achieved by state-of-the-art algorithms is only 16.3, which
reveals that we are still at a nascent stage for understanding objects,
instances, and videos in a real-world scenario. We also present a simple
plug-and-play module that performs temporal feature calibration to complement
missing object cues caused by occlusion. Built upon MaskTrack R-CNN and
SipMask, we obtain a remarkable AP improvement on the OVIS dataset. The OVIS
dataset and project code are available at http://songbai.site/ovis .