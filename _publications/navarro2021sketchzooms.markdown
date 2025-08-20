---
layout: publication
title: 'Sketchzooms: Deep Multi-view Descriptors For Matching Line Drawings'
authors: "Pablo Navarro, Jos\xE9 Ignacio Orlando, Claudio Delrieux, Emmanuel Iarussi"
conference: Computer Graphics Forum
year: 2021
bibkey: navarro2021sketchzooms
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.05019'}]
tags: [Neural Hashing]
short_authors: Navarro et al.
---
Finding point-wise correspondences between images is a long-standing problem
in image analysis. This becomes particularly challenging for sketch images, due
to the varying nature of human drawing style, projection distortions and
viewport changes. In this paper we present the first attempt to obtain a
learned descriptor for dense registration in line drawings. Based on recent
deep learning techniques for corresponding photographs, we designed descriptors
to locally match image pairs where the object of interest belongs to the same
semantic category, yet still differ drastically in shape, form, and projection
angle. To this end, we have specifically crafted a data set of synthetic
sketches using non-photorealistic rendering over a large collection of
part-based registered 3D models. After training, a neural network generates
descriptors for every pixel in an input image, which are shown to generalize
correctly in unseen sketches hand-drawn by humans. We evaluate our method
against a baseline of correspondences data collected from expert designers, in
addition to comparisons with other descriptors that have been proven effective
in sketches. Code, data and further resources will be publicly released by the
time of publication.