---
layout: publication
title: Learning Local Shape Descriptors From Part Correspondences With Multi-view
  Convolutional Networks
authors: Haibin Huang, Evangelos Kalogerakis, Siddhartha Chaudhuri, Duygu Ceylan,
  Vladimir G. Kim, Ersin Yumer
conference: Arxiv
year: 2017
bibkey: huang2017learning
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.04496'}]
tags: []
short_authors: Huang et al.
---
We present a new local descriptor for 3D shapes, directly applicable to a
wide range of shape analysis problems such as point correspondences, semantic
segmentation, affordance prediction, and shape-to-scan matching. The descriptor
is produced by a convolutional network that is trained to embed geometrically
and semantically similar points close to one another in descriptor space. The
network processes surface neighborhoods around points on a shape that are
captured at multiple scales by a succession of progressively zoomed out views,
taken from carefully selected camera positions. We leverage two extremely large
sources of data to train our network. First, since our network processes
rendered views in the form of 2D images, we repurpose architectures pre-trained
on massive image datasets. Second, we automatically generate a synthetic dense
point correspondence dataset by non-rigid alignment of corresponding shape
parts in a large collection of segmented 3D models. As a result of these design
choices, our network effectively encodes multi-scale local context and
fine-grained surface detail. Our network can be trained to produce either
category-specific descriptors or more generic descriptors by learning from
multiple shape categories. Once trained, at test time, the network extracts
local descriptors for shapes without requiring any part segmentation as input.
Our method can produce effective local descriptors even for shapes whose
category is unknown or different from the ones used while training. We
demonstrate through several experiments that our learned local descriptors are
more discriminative compared to state of the art alternatives, and are
effective in a variety of shape analysis applications.