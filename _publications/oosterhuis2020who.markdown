---
layout: publication
title: '"who Is Driving Around Me?" Unique Vehicle Instance Classification Using Deep
  Neural Features'
authors: Tim Oosterhuis, Lambert Schomaker
conference: Arxiv
year: 2020
bibkey: oosterhuis2020who
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.08771'}]
tags: []
short_authors: Tim Oosterhuis, Lambert Schomaker
---
Being aware of other traffic is a prerequisite for self-driving cars to
operate in the real world. In this paper, we show how the intrinsic feature
maps of an object detection CNN can be used to uniquely identify vehicles from
a dash-cam feed. Feature maps of a pretrained `YOLO' network are used to create
700 deep integrated feature signatures (DIFS) from 20 different images of 35
vehicles from a high resolution dataset and 340 signatures from 20 different
images of 17 vehicles of a lower resolution tracking benchmark dataset. The
YOLO network was trained to classify general object categories, e.g. classify a
detected object as a `car' or `truck'. 5-Fold nearest neighbor (1NN)
classification was used on DIFS created from feature maps in the middle layers
of the network to correctly identify unique vehicles at a rate of 96.7% for
the high resolution data and with a rate of 86.8% for the lower resolution
data. We conclude that a deep neural detection network trained to distinguish
between different classes can be successfully used to identify different
instances belonging to the same class, through the creation of deep integrated
feature signatures (DIFS).