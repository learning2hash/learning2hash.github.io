---
layout: publication
title: 'Epose: Let''s Make Efficientpose More Generally Applicable'
authors: Austin Lally, Robert Bain, Mazen Alotaibi
conference: Arxiv
year: 2021
bibkey: lally2021epose
citations: 0
additional_links: [{name: Code, url: 'https://github.com/tbd-clip/EfficientPose'},
  {name: Paper, url: 'https://arxiv.org/abs/2111.15114'}]
tags: []
short_authors: Austin Lally, Robert Bain, Mazen Alotaibi
---
EfficientPose is an impressive 3D object detection model. It has been
demonstrated to be quick, scalable, and accurate, especially when considering
that it uses only RGB inputs. In this paper we try to improve on EfficientPose
by giving it the ability to infer an object's size, and by simplifying both the
data collection and loss calculations. We evaluated ePose using the Linemod
dataset and a new subset of it called "Occlusion 1-class". We also outline our
current progress and thoughts about using ePose with the NuScenes and the 2017
KITTI 3D Object Detection datasets. The source code is available at
https://github.com/tbd-clip/EfficientPose.