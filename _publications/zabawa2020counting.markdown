---
layout: publication
title: Counting Of Grapevine Berries In Images Via Semantic Segmentation Using Convolutional
  Neural Networks
authors: "Laura Zabawa, Anna Kicherer, Lasse Klingbeil, Reinhard T\xF6pfer, Heiner\
  \ Kuhlmann, Ribana Roscher"
conference: ISPRS Journal of Photogrammetry and Remote Sensing
year: 2020
bibkey: zabawa2020counting
citations: 110
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.14010'}]
tags: []
short_authors: Zabawa et al.
---
The extraction of phenotypic traits is often very time and labour intensive.
Especially the investigation in viticulture is restricted to an on-site
analysis due to the perennial nature of grapevine. Traditionally skilled
experts examine small samples and extrapolate the results to a whole plot.
Thereby different grapevine varieties and training systems, e.g. vertical shoot
positioning (VSP) and semi minimal pruned hedges (SMPH) pose different
challenges. In this paper we present an objective framework based on automatic
image analysis which works on two different training systems. The images are
collected semi automatic by a camera system which is installed in a modified
grape harvester. The system produces overlapping images from the sides of the
plants. Our framework uses a convolutional neural network to detect single
berries in images by performing a semantic segmentation. Each berry is then
counted with a connected component algorithm. We compare our results with the
Mask-RCNN, a state-of-the-art network for instance segmentation and with a
regression approach for counting. The experiments presented in this paper show
that we are able to detect green berries in images despite of different
training systems. We achieve an accuracy for the berry detection of 94.0% in
the VSP and 85.6% in the SMPH.