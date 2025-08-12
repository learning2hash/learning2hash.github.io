---
layout: publication
title: Beyond Cartesian Representations For Local Descriptors
authors: Patrick Ebel, Anastasiia Mishchuk, Kwang Moo Yi, Pascal Fua, Eduard Trulls
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: ebel2019beyond
citations: 71
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.05547'}]
tags: ["ICCV"]
short_authors: Ebel et al.
---
The dominant approach for learning local patch descriptors relies on small
image regions whose scale must be properly estimated a priori by a keypoint
detector. In other words, if two patches are not in correspondence, their
descriptors will not match. A strategy often used to alleviate this problem is
to "pool" the pixel-wise features over log-polar regions, rather than regularly
spaced ones. By contrast, we propose to extract the "support region" directly
with a log-polar sampling scheme. We show that this provides us with a better
representation by simultaneously oversampling the immediate neighbourhood of
the point and undersampling regions far away from it. We demonstrate that this
representation is particularly amenable to learning descriptors with deep
networks. Our models can match descriptors across a much wider range of scales
than was possible before, and also leverage much larger support regions without
suffering from occlusions. We report state-of-the-art results on three
different datasets.