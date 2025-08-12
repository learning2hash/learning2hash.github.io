---
layout: publication
title: 'Sem-lsd: A Learning-based Semantic Line Segment Detector'
authors: Yi Sun, Xushen Han, Kai Sun, Boren Li, Yongjiang Chen, Mingyang Li
conference: Arxiv
year: 2019
bibkey: sun2019sem
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.06591'}]
tags: []
short_authors: Sun et al.
---
In this paper, we introduces a new type of line-shaped image representation,
named semantic line segment (Sem-LS) and focus on solving its detection
problem. Sem-LS contains high-level semantics and is a compact scene
representation where only visually salient line segments with stable semantics
are preserved. Combined with high-level semantics, Sem-LS is more robust under
cluttered environment compared with existing line-shaped representations. The
compactness of Sem-LS facilitates its use in large-scale applications, such as
city-scale SLAM (simultaneously localization and mapping) and LCD (loop closure
detection). Sem-LS detection is a challenging task due to its significantly
different appearance from existing learning-based image representations such as
wireframes and objects. For further investigation, we first label Sem-LS on two
well-known datasets, KITTI and KAIST URBAN, as new benchmarks. Then, we propose
a learning-based Sem-LS detector (Sem-LSD) and devise new module as well as
metrics to address unique challenges in Sem-LS detection. Experimental results
have shown both the efficacy and efficiency of Sem-LSD. Finally, the
effectiveness of the proposed Sem-LS is supported by two experiments on
detector repeatability and a city-scale LCD problem. Labeled datasets and code
will be released shortly.