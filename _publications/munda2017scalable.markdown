---
layout: publication
title: Scalable Full Flow With Learned Binary Descriptors
authors: "Gottfried Munda, Alexander Shekhovtsov, Patrick Kn\xF6belreiter, Thomas\
  \ Pock"
conference: Lecture Notes in Computer Science
year: 2017
bibkey: munda2017scalable
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.06427'}]
tags: []
short_authors: Munda et al.
---
We propose a method for large displacement optical flow in which local
matching costs are learned by a convolutional neural network (CNN) and a
smoothness prior is imposed by a conditional random field (CRF). We tackle the
computation- and memory-intensive operations on the 4D cost volume by a
min-projection which reduces memory complexity from quadratic to linear and
binary descriptors for efficient matching. This enables evaluation of the cost
on the fly and allows to perform learning and CRF inference on high resolution
images without ever storing the 4D cost volume. To address the problem of
learning binary descriptors we propose a new hybrid learning scheme. In
contrast to current state of the art approaches for learning binary CNNs we can
compute the exact non-zero gradient within our model. We compare several
methods for training binary descriptors and show results on public available
benchmarks.