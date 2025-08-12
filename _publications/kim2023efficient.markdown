---
layout: publication
title: Efficient Semantic Matching With Hypercolumn Correlation
authors: Seungwook Kim, Juhong Min, Minsu Cho
conference: 2024 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2024
bibkey: kim2023efficient
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.04336'}]
tags: []
short_authors: Seungwook Kim, Juhong Min, Minsu Cho
---
Recent studies show that leveraging the match-wise relationships within the
4D correlation map yields significant improvements in establishing semantic
correspondences - but at the cost of increased computation and latency. In this
work, we focus on the aspect that the performance improvements of recent
methods can also largely be attributed to the usage of multi-scale correlation
maps, which hold various information ranging from low-level geometric cues to
high-level semantic contexts. To this end, we propose HCCNet, an efficient yet
effective semantic matching method which exploits the full potential of
multi-scale correlation maps, while eschewing the reliance on expensive
match-wise relationship mining on the 4D correlation map. Specifically, HCCNet
performs feature slicing on the bottleneck features to yield a richer set of
intermediate features, which are used to construct a hypercolumn correlation.
HCCNet can consequently establish semantic correspondences in an effective
manner by reducing the volume of conventional high-dimensional convolution or
self-attention operations to efficient point-wise convolutions. HCCNet
demonstrates state-of-the-art or competitive performances on the standard
benchmarks of semantic matching, while incurring a notably lower latency and
computation overhead compared to the existing SoTA methods.