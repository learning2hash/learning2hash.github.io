---
layout: publication
title: Counting Grid Aggregation For Event Retrieval And Recognition
authors: Zhanning Gao, Gang Hua, Dongqing Zhang, Jianru Xue, Nanning Zheng
conference: Arxiv
year: 2016
bibkey: gao2016counting
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.01109'}]
tags: [Evaluation]
short_authors: Gao et al.
---
Event retrieval and recognition in a large corpus of videos necessitates a
holistic fixed-size visual representation at the video clip level that is
comprehensive, compact, and yet discriminative. It shall comprehensively
aggregate information across relevant video frames, while suppress redundant
information, leading to a compact representation that can effectively
differentiate among different visual events. In search for such a
representation, we propose to build a spatially consistent counting grid model
to aggregate together deep features extracted from different video frames. The
spatial consistency of the counting grid model is achieved by introducing a
prior model estimated from a large corpus of video data. The counting grid
model produces an intermediate tensor representation for each video, which
automatically identifies and removes the feature redundancy across the
different frames. The tensor representation is subsequently reduced to a
fixed-size vector representation by averaging over the counting grid. When
compared to existing methods on both event retrieval and event classification
benchmarks, we achieve significantly better accuracy with much more compact
representation.