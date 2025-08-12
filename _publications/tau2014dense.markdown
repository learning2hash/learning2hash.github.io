---
layout: publication
title: Dense Correspondences Across Scenes And Scales
authors: Moria Tau, Tal Hassner
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2015
bibkey: tau2014dense
citations: 49
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1406.6323'}]
tags: []
short_authors: Moria Tau, Tal Hassner
---
We seek a practical method for establishing dense correspondences between two
images with similar content, but possibly different 3D scenes. One of the
challenges in designing such a system is the local scale differences of objects
appearing in the two images. Previous methods often considered only small
subsets of image pixels; matching only pixels for which stable scales may be
reliably estimated. More recently, others have considered dense
correspondences, but with substantial costs associated with generating, storing
and matching scale invariant descriptors. Our work here is motivated by the
observation that pixels in the image have contexts -- the pixels around them --
which may be exploited in order to estimate local scales reliably and
repeatably. Specifically, we make the following contributions. (i) We show that
scales estimated in sparse interest points may be propagated to neighboring
pixels where this information cannot be reliably determined. Doing so allows
scale invariant descriptors to be extracted anywhere in the image, not just in
detected interest points. (ii) We present three different means for propagating
this information: using only the scales at detected interest points, using the
underlying image information to guide the propagation of this information
across each image, separately, and using both images simultaneously. Finally,
(iii), we provide extensive results, both qualitative and quantitative,
demonstrating that accurate dense correspondences can be obtained even between
very different images, with little computational costs beyond those required by
existing methods.