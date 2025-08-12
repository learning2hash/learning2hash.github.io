---
layout: publication
title: Long-term Visual Localization Using Semantically Segmented Images
authors: Erik Stenborg, Carl Toft, Lars Hammarstrand
conference: 2018 IEEE International Conference on Robotics and Automation (ICRA)
year: 2018
bibkey: stenborg2018long
citations: 110
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.05269'}]
tags: ["ICRA"]
short_authors: Erik Stenborg, Carl Toft, Lars Hammarstrand
---
Robust cross-seasonal localization is one of the major challenges in
long-term visual navigation of autonomous vehicles. In this paper, we exploit
recent advances in semantic segmentation of images, i.e., where each pixel is
assigned a label related to the type of object it represents, to attack the
problem of long-term visual localization. We show that semantically labeled 3-D
point maps of the environment, together with semantically segmented images, can
be efficiently used for vehicle localization without the need for detailed
feature descriptors (SIFT, SURF, etc.). Thus, instead of depending on
hand-crafted feature descriptors, we rely on the training of an image
segmenter. The resulting map takes up much less storage space compared to a
traditional descriptor based map. A particle filter based semantic localization
solution is compared to one based on SIFT-features, and even with large
seasonal variations over the year we perform on par with the larger and more
descriptive SIFT-features, and are able to localize with an error below 1 m
most of the time.