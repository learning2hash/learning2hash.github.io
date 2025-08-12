---
layout: publication
title: 'Scene Categorization From Contours: Medial Axis Based Salience Measures'
authors: Morteza Rezanejad, Gabriel Downs, John Wilder, Dirk B. Walther, Allan Jepson,
  Sven Dickinson, Kaleem Siddiqi
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: rezanejad2018scene
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.10524'}]
tags: ["CVPR"]
short_authors: Rezanejad et al.
---
The computer vision community has witnessed recent advances in scene
categorization from images, with the state-of-the art systems now achieving
impressive recognition rates on challenging benchmarks such as the Places365
dataset. Such systems have been trained on photographs which include color,
texture and shading cues. The geometry of shapes and surfaces, as conveyed by
scene contours, is not explicitly considered for this task. Remarkably, humans
can accurately recognize natural scenes from line drawings, which consist
solely of contour-based shape cues. Here we report the first computer vision
study on scene categorization of line drawings derived from popular databases
including an artist scene database, MIT67, and Places365. Specifically, we use
off-the-shelf pre-trained CNNs to perform scene classification given only
contour information as input and find performance levels well above chance. We
also show that medial-axis based contour salience methods can be used to select
more informative subsets of contour pixels and that the variation in CNN
classification performance on various choices for these subsets is
qualitatively similar to that observed in human performance. Moreover, when the
salience measures are used to weight the contours, as opposed to pruning them,
we find that these weights boost our CNN performance above that for unweighted
contour input. That is, the medial axis based salience weights appear to add
useful information that is not available when CNNs are trained to use contours
alone.