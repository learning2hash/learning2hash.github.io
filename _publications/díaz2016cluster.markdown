---
layout: publication
title: Cluster-wise Ratio Tests For Fast Camera Localization
authors: "Ra\xFAl D\xEDaz, Charless C. Fowlkes"
conference: Arxiv
year: 2016
bibkey: "d\xEDaz2016cluster"
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.01689'}]
tags: ["Evaluation", "Scalability"]
short_authors: "Ra\xFAl D\xEDaz, Charless C. Fowlkes"
---
Feature point matching for camera localization suffers from scalability
problems. Even when feature descriptors associated with 3D scene points are
locally unique, as coverage grows, similar or repeated features become
increasingly common. As a result, the standard distance ratio-test used to
identify reliable image feature points is overly restrictive and rejects many
good candidate matches. We propose a simple coarse-to-fine strategy that uses
conservative approximations to robust local ratio-tests that can be computed
efficiently using global approximate k-nearest neighbor search. We treat these
forward matches as votes in camera pose space and use them to prioritize
back-matching within candidate camera pose clusters, exploiting feature
co-visibility captured by clustering the 3D model camera pose graph. This
approach achieves state-of-the-art camera localization results on a variety of
popular benchmarks, outperforming several methods that use more complicated
data structures and that make more restrictive assumptions on camera pose. We
also carry out diagnostic analyses on a difficult test dataset containing
globally repetitive structure that suggest our approach successfully adapts to
the challenges of large-scale image localization.