---
layout: publication
title: 'Learning To Separate: Detecting Heavily-occluded Objects In Urban Scenes'
authors: Chenhongyi Yang, Vitaly Ablavsky, Kaihong Wang, Qi Feng, Margrit Betke
conference: ACM Transactions on Multimedia Computing, Communications, and Applications
year: 2020
bibkey: yang2020learning
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.01674'}]
tags: ["Datasets", "Recommender Systems", "Similarity Search"]
short_authors: Yang et al.
---
While visual object detection with deep learning has received much attention
in the past decade, cases when heavy intra-class occlusions occur have not been
studied thoroughly. In this work, we propose a Non-Maximum-Suppression (NMS)
algorithm that dramatically improves the detection recall while maintaining
high precision in scenes with heavy occlusions. Our NMS algorithm is derived
from a novel embedding mechanism, in which the semantic and geometric features
of the detected boxes are jointly exploited. The embedding makes it possible to
determine whether two heavily-overlapping boxes belong to the same object in
the physical world. Our approach is particularly useful for car detection and
pedestrian detection in urban scenes where occlusions often happen. We show the
effectiveness of our approach by creating a model called SG-Det (short for
Semantics and Geometry Detection) and testing SG-Det on two widely-adopted
datasets, KITTI and CityPersons for which it achieves state-of-the-art
performance.