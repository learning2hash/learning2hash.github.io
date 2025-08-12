---
layout: publication
title: Improving The Accuracy Of Nearest-neighbor Classification Using Principled
  Construction And Stochastic Sampling Of Training-set Centroids
authors: Stephen Whitelam
conference: Entropy 23 149 (2021)
year: 2018
bibkey: whitelam2018improving
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.02599'}]
tags: ["Evaluation"]
short_authors: Stephen Whitelam
---
A conceptually simple way to classify images is to directly compare test-set
data and training-set data. The accuracy of this approach is limited by the
method of comparison used, and by the extent to which the training-set data
cover configuration space. Here we show that this coverage can be substantially
increased using coarse graining (replacing groups of images by their centroids)
and stochastic sampling (using distinct sets of centroids in combination). We
use the MNIST and Fashion-MNIST data sets to show that a principled
coarse-graining algorithm can convert training images into fewer image
centroids without loss of accuracy of classification of test-set images by
nearest-neighbor classification. Distinct batches of centroids can be used in
combination as a means of stochastically sampling configuration space, and can
classify test-set data more accurately than can the unaltered training set. On
the MNIST and Fashion-MNIST data sets this approach converts nearest-neighbor
classification from a mid-ranking- to an upper-ranking member of the set of
classical machine-learning techniques.