---
layout: publication
title: Learned Multi-patch Similarity
authors: Wilfried Hartmann, Silvano Galliani, Michal Havlena, Luc van Gool, Konrad
  Schindler
conference: 2017 IEEE International Conference on Computer Vision (ICCV)
year: 2017
bibkey: hartmann2017learned
citations: 121
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.08836'}]
tags: ["ICCV"]
short_authors: Hartmann et al.
---
Estimating a depth map from multiple views of a scene is a fundamental task
in computer vision. As soon as more than two viewpoints are available, one
faces the very basic question how to measure similarity across >2 image
patches. Surprisingly, no direct solution exists, instead it is common to fall
back to more or less robust averaging of two-view similarities. Encouraged by
the success of machine learning, and in particular convolutional neural
networks, we propose to learn a matching function which directly maps multiple
image patches to a scalar similarity score. Experiments on several multi-view
datasets demonstrate that this approach has advantages over methods based on
pairwise patch similarity.