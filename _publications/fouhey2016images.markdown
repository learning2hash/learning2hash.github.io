---
layout: publication
title: From Images To 3D Shape Attributes
authors: David F. Fouhey, Abhinav Gupta, Andrew Zisserman
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2017
bibkey: fouhey2016images
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.06836'}]
tags: []
short_authors: David F. Fouhey, Abhinav Gupta, Andrew Zisserman
---
Our goal in this paper is to investigate properties of 3D shape that can be
determined from a single image. We define 3D shape attributes -- generic
properties of the shape that capture curvature, contact and occupied space. Our
first objective is to infer these 3D shape attributes from a single image. A
second objective is to infer a 3D shape embedding -- a low dimensional vector
representing the 3D shape.
  We study how the 3D shape attributes and embedding can be obtained from a
single image by training a Convolutional Neural Network (CNN) for this task. We
start with synthetic images so that the contribution of various cues and
nuisance parameters can be controlled. We then turn to real images and
introduce a large scale image dataset of sculptures containing 143K images
covering 2197 works from 242 artists.
  For the CNN trained on the sculpture dataset we show the following: (i) which
regions of the imaged sculpture are used by the CNN to infer the 3D shape
attributes; (ii) that the shape embedding can be used to match previously
unseen sculptures largely independent of viewpoint; and (iii) that the 3D
attributes generalize to images of other (non-sculpture) object classes.