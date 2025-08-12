---
layout: publication
title: Illumination-insensitive Binary Descriptor For Visual Measurement Based On
  Local Inter-patch Invariance
authors: Xinyu Lin, Yingjie Zhou, Xun Zhang, Yipeng Liu, Ce Zhu
conference: IEEE Transactions on Instrumentation and Measurement
year: 2023
bibkey: lin2023illumination
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.07943'}]
tags: []
short_authors: Lin et al.
---
Binary feature descriptors have been widely used in various visual
measurement tasks, particularly those with limited computing resources and
storage capacities. Existing binary descriptors may not perform well for
long-term visual measurement tasks due to their sensitivity to illumination
variations. It can be observed that when image illumination changes
dramatically, the relative relationship among local patches mostly remains
intact. Based on the observation, consequently, this study presents an
illumination-insensitive binary (IIB) descriptor by leveraging the local
inter-patch invariance exhibited in multiple spatial granularities to deal with
unfavorable illumination variations. By taking advantage of integral images for
local patch feature computation, a highly efficient IIB descriptor is achieved.
It can encode scalable features in multiple spatial granularities, thus
facilitating a computationally efficient hierarchical matching from coarse to
fine. Moreover, the IIB descriptor can also apply to other types of image data,
such as depth maps and semantic segmentation results, when available in some
applications. Numerical experiments on both natural and synthetic datasets
reveal that the proposed IIB descriptor outperforms state-of-the-art binary
descriptors and some testing float descriptors. The proposed IIB descriptor has
also been successfully employed in a demo system for long-term visual
localization. The code of the IIB descriptor will be publicly available.