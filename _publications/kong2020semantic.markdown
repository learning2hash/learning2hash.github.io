---
layout: publication
title: Semantic Graph Based Place Recognition For 3D Point Clouds
authors: Xin Kong, Xuemeng Yang, Guangyao Zhai, Xiangrui Zhao, Xianfang Zeng, Mengmeng
  Wang, Yong Liu, Wanlong Li, Feng Wen
conference: 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems
  (IROS)
year: 2020
bibkey: kong2020semantic
citations: 97
additional_links: [{name: Code, url: 'https://github.com/kxhit/SG_PR'}, {name: Paper,
    url: 'https://arxiv.org/abs/2008.11459'}]
tags: ["IROS", "Robustness"]
short_authors: Kong et al.
---
Due to the difficulty in generating the effective descriptors which are
robust to occlusion and viewpoint changes, place recognition for 3D point cloud
remains an open issue. Unlike most of the existing methods that focus on
extracting local, global, and statistical features of raw point clouds, our
method aims at the semantic level that can be superior in terms of robustness
to environmental changes. Inspired by the perspective of humans, who recognize
scenes through identifying semantic objects and capturing their relations, this
paper presents a novel semantic graph based approach for place recognition.
First, we propose a novel semantic graph representation for the point cloud
scenes by reserving the semantic and topological information of the raw point
cloud. Thus, place recognition is modeled as a graph matching problem. Then we
design a fast and effective graph similarity network to compute the similarity.
Exhaustive evaluations on the KITTI dataset show that our approach is robust to
the occlusion as well as viewpoint changes and outperforms the state-of-the-art
methods with a large margin. Our code is available at:
https://github.com/kxhit/SG_PR.