---
layout: publication
title: Camera Bias In A Fine Grained Classification Task
authors: Philip T. Jackson, Stephen Bonner, Ning Jia, Christopher Holder, Jon Stonehouse,
  Boguslaw Obara
conference: Arxiv
year: 2020
bibkey: jackson2020camera
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.08574'}]
tags: []
short_authors: Jackson et al.
---
We show that correlations between the camera used to acquire an image and the
class label of that image can be exploited by convolutional neural networks
(CNN), resulting in a model that "cheats" at an image classification task by
recognizing which camera took the image and inferring the class label from the
camera. We show that models trained on a dataset with camera / label
correlations do not generalize well to images in which those correlations are
absent, nor to images from unencountered cameras. Furthermore, we investigate
which visual features they are exploiting for camera recognition. Our
experiments present evidence against the importance of global color statistics,
lens deformation and chromatic aberration, and in favor of high frequency
features, which may be introduced by image processing algorithms built into the
cameras.