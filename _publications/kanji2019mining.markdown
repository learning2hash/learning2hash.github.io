---
layout: publication
title: Mining Minimal Map-segments For Visual Place Classifiers
authors: Tanaka Kanji
conference: Arxiv
year: 2019
bibkey: kanji2019mining
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.09594'}]
tags: []
short_authors: Tanaka Kanji
---
In visual place recognition (VPR), map segmentation (MS) is a preprocessing
technique used to partition a given view-sequence map into place classes (i.e.,
map segments) so that each class has good place-specific training images for a
visual place classifier (VPC). Existing approaches to MS implicitly/explicitly
suppose that map segments have a certain size, or individual map segments are
balanced in size. However, recent VPR systems showed that very small important
map segments (minimal map segments) often suffice for VPC, and the remaining
large unimportant portion of the map should be discarded to minimize map
maintenance cost. Here, a new MS algorithm that can mine minimal map segments
from a large view-sequence map is presented. To solve the inherently NP hard
problem, MS is formulated as a video-segmentation problem and the efficient
point-trajectory based paradigm of video segmentation is used. The proposed map
representation was implemented with three types of VPC: deep convolutional
neural network, bag-of-words, and object class detector, and each was
integrated into a Monte Carlo localization algorithm (MCL) within a topometric
VPR framework. Experiments using the publicly available NCLT dataset thoroughly
investigate the efficacy of MS in terms of VPR performance.