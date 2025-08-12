---
layout: publication
title: Bootstrapped Cnns For Building Segmentation On RGB-D Aerial Imagery
authors: Clint Sebastian, Bas Boom, Thijs van Lankveld, Egor Bondarev, Peter H. N.
  de With
conference: ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Information
  Sciences
year: 2018
bibkey: sebastian2018bootstrapped
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.03570'}]
tags: ["Datasets", "Evaluation"]
short_authors: Sebastian et al.
---
Detection of buildings and other objects from aerial images has various
applications in urban planning and map making. Automated building detection
from aerial imagery is a challenging task, as it is prone to varying lighting
conditions, shadows and occlusions. Convolutional Neural Networks (CNNs) are
robust against some of these variations, although they fail to distinguish easy
and difficult examples. We train a detection algorithm from RGB-D images to
obtain a segmented mask by using the CNN architecture DenseNet.First, we
improve the performance of the model by applying a statistical re-sampling
technique called Bootstrapping and demonstrate that more informative examples
are retained. Second, the proposed method outperforms the non-bootstrapped
version by utilizing only one-sixth of the original training data and it
obtains a precision-recall break-even of 95.10% on our aerial imagery dataset.