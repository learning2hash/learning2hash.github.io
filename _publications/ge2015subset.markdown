---
layout: publication
title: Subset Feature Learning For Fine-grained Category Classification
authors: Zongyuan Ge, Christopher McCool, Conrad Sanderson, Peter Corke
conference: 2015 IEEE Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2015
bibkey: ge2015subset
citations: 53
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1505.02269'}]
tags: ["CVPR"]
short_authors: Ge et al.
---
Fine-grained categorisation has been a challenging problem due to small
inter-class variation, large intra-class variation and low number of training
images. We propose a learning system which first clusters visually similar
classes and then learns deep convolutional neural network features specific to
each subset. Experiments on the popular fine-grained Caltech-UCSD bird dataset
show that the proposed method outperforms recent fine-grained categorisation
methods under the most difficult setting: no bounding boxes are presented at
test time. It achieves a mean accuracy of 77.5%, compared to the previous best
performance of 73.2%. We also show that progressive transfer learning allows us
to first learn domain-generic features (for bird classification) which can then
be adapted to specific set of bird classes, yielding improvements in accuracy.