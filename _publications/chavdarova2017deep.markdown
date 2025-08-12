---
layout: publication
title: Deep Multi-camera People Detection
authors: "Tatjana Chavdarova, Fran\xE7ois Fleuret"
conference: 2017 16th IEEE International Conference on Machine Learning and Applications
  (ICMLA)
year: 2017
bibkey: chavdarova2017deep
citations: 55
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.04593'}]
tags: []
short_authors: "Tatjana Chavdarova, Fran\xE7ois Fleuret"
---
This paper addresses the problem of multi-view people occupancy map
estimation. Existing solutions for this problem either operate per-view, or
rely on a background subtraction pre-processing. Both approaches lessen the
detection performance as scenes become more crowded. The former does not
exploit joint information, whereas the latter deals with ambiguous input due to
the foreground blobs becoming more and more interconnected as the number of
targets increases.
  Although deep learning algorithms have proven to excel on remarkably numerous
computer vision tasks, such a method has not been applied yet to this problem.
In large part this is due to the lack of large-scale multi-camera data-set.
  The core of our method is an architecture which makes use of monocular
pedestrian data-set, available at larger scale then the multi-view ones,
applies parallel processing to the multiple video streams, and jointly utilises
it. Our end-to-end deep learning method outperforms existing methods by large
margins on the commonly used PETS 2009 data-set. Furthermore, we make publicly
available a new three-camera HD data-set. Our source code and trained models
will be made available under an open-source license.