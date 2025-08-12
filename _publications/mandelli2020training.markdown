---
layout: publication
title: 'Training Cnns In Presence Of JPEG Compression: Multimedia Forensics Vs Computer
  Vision'
authors: "Sara Mandelli, Nicol\xF2 Bonettini, Paolo Bestagini, Stefano Tubaro"
conference: 2020 IEEE International Workshop on Information Forensics and Security
  (WIFS)
year: 2020
bibkey: mandelli2020training
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.12088'}]
tags: []
short_authors: Mandelli et al.
---
Convolutional Neural Networks (CNNs) have proved very accurate in multiple
computer vision image classification tasks that required visual inspection in
the past (e.g., object recognition, face detection, etc.). Motivated by these
astonishing results, researchers have also started using CNNs to cope with
image forensic problems (e.g., camera model identification, tampering
detection, etc.). However, in computer vision, image classification methods
typically rely on visual cues easily detectable by human eyes. Conversely,
forensic solutions rely on almost invisible traces that are often very subtle
and lie in the fine details of the image under analysis. For this reason,
training a CNN to solve a forensic task requires some special care, as common
processing operations (e.g., resampling, compression, etc.) can strongly hinder
forensic traces. In this work, we focus on the effect that JPEG has on CNN
training considering different computer vision and forensic image
classification problems. Specifically, we consider the issues that rise from
JPEG compression and misalignment of the JPEG grid. We show that it is
necessary to consider these effects when generating a training dataset in order
to properly train a forensic detector not losing generalization capability,
whereas it is almost possible to ignore these effects for computer vision
tasks.