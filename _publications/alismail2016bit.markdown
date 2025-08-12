---
layout: publication
title: 'Bit-planes: Dense Subpixel Alignment Of Binary Descriptors'
authors: Hatem Alismail, Brett Browning, Simon Lucey
conference: Arxiv
year: 2016
bibkey: alismail2016bit
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.00307'}]
tags: []
short_authors: Hatem Alismail, Brett Browning, Simon Lucey
---
Binary descriptors have been instrumental in the recent evolution of
computationally efficient sparse image alignment algorithms. Increasingly,
however, the vision community is interested in dense image alignment methods,
which are more suitable for estimating correspondences from high frame rate
cameras as they do not rely on exhaustive search. However, classic dense
alignment approaches are sensitive to illumination change. In this paper, we
propose an easy to implement and low complexity dense binary descriptor, which
we refer to as bit-planes, that can be seamlessly integrated within a
multi-channel Lucas & Kanade framework. This novel approach combines the
robustness of binary descriptors with the speed and accuracy of dense alignment
methods. The approach is demonstrated on a template tracking problem achieving
state-of-the-art robustness and faster than real-time performance on consumer
laptops (400+ fps on a single core Intel i7) and hand-held mobile devices (100+
fps on an iPad Air 2).