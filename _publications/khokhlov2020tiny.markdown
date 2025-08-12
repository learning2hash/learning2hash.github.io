---
layout: publication
title: Tiny-yolo Object Detection Supplemented With Geometrical Data
authors: Ivan Khokhlov, Egor Davydenko, Ilya Osokin, Ilya Ryakin, Azer Babaev, Vladimir
  Litvinenko, Roman Gorbachev
conference: 2020 IEEE 91st Vehicular Technology Conference (VTC2020-Spring)
year: 2020
bibkey: khokhlov2020tiny
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.02170'}]
tags: ["Evaluation"]
short_authors: Khokhlov et al.
---
We propose a method of improving detection precision (mAP) with the help of
the prior knowledge about the scene geometry: we assume the scene to be a plane
with objects placed on it. We focus our attention on autonomous robots, so
given the robot's dimensions and the inclination angles of the camera, it is
possible to predict the spatial scale for each pixel of the input frame. With
slightly modified YOLOv3-tiny we demonstrate that the detection supplemented by
the scale channel, further referred as S, outperforms standard RGB-based
detection with small computational overhead.