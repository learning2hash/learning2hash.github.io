---
layout: publication
title: 'Scone: Siamese Constellation Embedding Descriptor For Image Matching'
authors: Tomasz Trzcinski, Jacek Komorowski, Lukasz Dabala, Konrad Czarnota, Grzegorz
  Kurzejamski, Simon Lynen
conference: Lecture Notes in Computer Science
year: 2019
bibkey: trzcinski2018scone
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.11054'}]
tags: []
short_authors: Trzcinski et al.
---
Numerous computer vision applications rely on local feature descriptors, such
as SIFT, SURF or FREAK, for image matching. Although their local character
makes image matching processes more robust to occlusions, it often leads to
geometrically inconsistent keypoint matches that need to be filtered out, e.g.
using RANSAC. In this paper we propose a novel, more discriminative, descriptor
that includes not only local feature representation, but also information about
the geometric layout of neighbouring keypoints. To that end, we use a Siamese
architecture that learns a low-dimensional feature embedding of keypoint
constellation by maximizing the distances between non-corresponding pairs of
matched image patches, while minimizing it for correct matches. The
48-dimensional oating point descriptor that we train is built on top of the
state-of-the-art FREAK descriptor achieves significant performance improvement
over the competitors on a challenging TUM dataset.