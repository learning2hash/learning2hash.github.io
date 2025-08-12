---
layout: publication
title: 'In Pixels We Trust: From Pixel Labeling To Object Localization And Scene Categorization'
authors: "Carlos Herranz-Perdiguero, Carolina Redondo-Cabrera, Roberto J. L\xF3pez-Sastre"
conference: 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems
  (IROS)
year: 2018
bibkey: herranzperdiguero2018pixels
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.07284'}]
tags: ["IROS"]
short_authors: "Carlos Herranz-Perdiguero, Carolina Redondo-Cabrera, Roberto J. L\xF3\
  pez-Sastre"
---
While there has been significant progress in solving the problems of image
pixel labeling, object detection and scene classification, existing approaches
normally address them separately. In this paper, we propose to tackle these
problems from a bottom-up perspective, where we simply need a semantic
segmentation of the scene as input. We employ the DeepLab architecture, based
on the ResNet deep network, which leverages multi-scale inputs to later fuse
their responses to perform a precise pixel labeling of the scene. This semantic
segmentation mask is used to localize the objects and to recognize the scene,
following two simple yet effective strategies. We evaluate the benefits of our
solutions, performing a thorough experimental evaluation on the NYU Depth V2
dataset. Our approach achieves a performance that beats the leading results by
a significant margin, defining the new state of the art in this benchmark for
the three tasks comprising the scene understanding: semantic segmentation,
object detection and scene categorization.