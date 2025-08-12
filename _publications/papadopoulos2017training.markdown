---
layout: publication
title: Training Object Class Detectors With Click Supervision
authors: Dim P. Papadopoulos, Jasper R. R. Uijlings, Frank Keller, Vittorio Ferrari
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: papadopoulos2017training
citations: 111
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.06189'}]
tags: ["CVPR", "Supervised"]
short_authors: Papadopoulos et al.
---
Training object class detectors typically requires a large set of images with
objects annotated by bounding boxes. However, manually drawing bounding boxes
is very time consuming. In this paper we greatly reduce annotation time by
proposing center-click annotations: we ask annotators to click on the center of
an imaginary bounding box which tightly encloses the object instance. We then
incorporate these clicks into existing Multiple Instance Learning techniques
for weakly supervised object localization, to jointly localize object bounding
boxes over all training images. Extensive experiments on PASCAL VOC 2007 and MS
COCO show that: (1) our scheme delivers high-quality detectors, performing
substantially better than those produced by weakly supervised techniques, with
a modest extra annotation effort; (2) these detectors in fact perform in a
range close to those trained from manually drawn bounding boxes; (3) as the
center-click task is very fast, our scheme reduces total annotation time by 9x
to 18x.