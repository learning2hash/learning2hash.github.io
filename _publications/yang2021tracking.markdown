---
layout: publication
title: Tracking Instances As Queries
authors: Shusheng Yang, Yuxin Fang, Xinggang Wang, Yu Li, Ying Shan, Bin Feng, Wenyu
  Liu
conference: CVPR 2021 Workshop. 2nd Place Solution for YouTube-VOS Challenge 2021
  Video Instance Segmentation
year: 2021
bibkey: yang2021tracking
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.11963'}]
tags: ["CVPR"]
short_authors: Yang et al.
---
Recently, query based deep networks catch lots of attention owing to their
end-to-end pipeline and competitive results on several fundamental computer
vision tasks, such as object detection, semantic segmentation, and instance
segmentation. However, how to establish a query based video instance
segmentation (VIS) framework with elegant architecture and strong performance
remains to be settled. In this paper, we present \textbf\{QueryTrack\} (i.e.,
tracking instances as queries), a unified query based VIS framework fully
leveraging the intrinsic one-to-one correspondence between instances and
queries in QueryInst. The proposed method obtains 52.7 / 52.3 AP on
YouTube-VIS-2019 / 2021 datasets, which wins the 2-nd place in the YouTube-VIS
Challenge at CVPR 2021 \textbf\{with a single online end-to-end model, single
scale testing \& modest amount of training data\}. We also provide
QueryTrack-ResNet-50 baseline results on YouTube-VIS-2021 val set as references
for the VIS community.