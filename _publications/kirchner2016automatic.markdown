---
layout: publication
title: Automatic Thresholding Of SIFT Descriptors
authors: Matthew R. Kirchner
conference: 2016 IEEE International Conference on Image Processing (ICIP)
year: 2016
bibkey: kirchner2016automatic
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.03173'}]
tags: []
short_authors: Matthew R. Kirchner
---
We introduce a method to perform automatic thresholding of SIFT descriptors
that improves matching performance by at least 15.9% on the Oxford image
matching benchmark. The method uses a contrario methodology to determine a
unique bin magnitude threshold. This is done by building a generative uniform
background model for descriptors and determining when bin magnitudes have
reached a sufficient level. The presented method, called meaningful clamping,
contrasts from the current SIFT implementation by efficiently computing a
clamping threshold that is unique for every descriptor.