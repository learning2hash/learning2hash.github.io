---
layout: publication
title: Machine Learning On Images Using A String-distance
authors: Uzi Chester, Joel Ratsaby
conference: Arxiv
year: 2013
bibkey: chester2013machine
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1305.4204'}]
tags: []
short_authors: Uzi Chester, Joel Ratsaby
---
We present a new method for image feature-extraction which is based on
representing an image by a finite-dimensional vector of distances that measure
how different the image is from a set of image prototypes. We use the recently
introduced Universal Image Distance (UID) \cite\{RatsabyChesterIEEE2012\} to
compare the similarity between an image and a prototype image. The advantage in
using the UID is the fact that no domain knowledge nor any image analysis need
to be done. Each image is represented by a finite dimensional feature vector
whose components are the UID values between the image and a finite set of image
prototypes from each of the feature categories. The method is automatic since
once the user selects the prototype images, the feature vectors are
automatically calculated without the need to do any image analysis. The
prototype images can be of different size, in particular, different than the
image size. Based on a collection of such cases any supervised or unsupervised
learning algorithm can be used to train and produce an image classifier or
image cluster analysis. In this paper we present the image feature-extraction
method and use it on several supervised and unsupervised learning experiments
for satellite image data.