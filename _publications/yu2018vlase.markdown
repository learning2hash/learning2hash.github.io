---
layout: publication
title: 'VLASE: Vehicle Localization By Aggregating Semantic Edges'
authors: Xin Yu, Sagar Chaturvedi, Chen Feng, Yuichi Taguchi, Teng-Yok Lee, Clinton
  Fernandes, Srikumar Ramalingam
conference: 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems
  (IROS)
year: 2018
bibkey: yu2018vlase
citations: 40
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.02536'}]
tags: ["Evaluation", "IROS", "Image Retrieval", "Tools & Libraries"]
short_authors: Yu et al.
---
In this paper, we propose VLASE, a framework to use semantic edge features
from images to achieve on-road localization. Semantic edge features denote edge
contours that separate pairs of distinct objects such as building-sky, road-
sidewalk, and building-ground. While prior work has shown promising results by
utilizing the boundary between prominent classes such as sky and building using
skylines, we generalize this approach to consider semantic edge features that
arise from 19 different classes. Our localization algorithm is simple, yet very
powerful. We extract semantic edge features using a recently introduced CASENet
architecture and utilize VLAD framework to perform image retrieval. Our
experiments show that we achieve improvement over some of the state-of-the-art
localization algorithms such as SIFT-VLAD and its deep variant NetVLAD. We use
ablation study to study the importance of different semantic classes and show
that our unified approach achieves better performance compared to individual
prominent features such as skylines.