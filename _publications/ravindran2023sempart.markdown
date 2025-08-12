---
layout: publication
title: 'SEMPART: Self-supervised Multi-resolution Partitioning Of Image Semantics'
authors: Sriram Ravindran, Debraj Basu
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: ravindran2023sempart
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.10972'}]
tags: ["ICCV", "Self-Supervised", "Unsupervised"]
short_authors: Sriram Ravindran, Debraj Basu
---
Accurately determining salient regions of an image is challenging when
labeled data is scarce. DINO-based self-supervised approaches have recently
leveraged meaningful image semantics captured by patch-wise features for
locating foreground objects. Recent methods have also incorporated intuitive
priors and demonstrated value in unsupervised methods for object partitioning.
In this paper, we propose SEMPART, which jointly infers coarse and fine
bi-partitions over an image's DINO-based semantic graph. Furthermore, SEMPART
preserves fine boundary details using graph-driven regularization and
successfully distills the coarse mask semantics into the fine mask. Our salient
object detection and single object localization findings suggest that SEMPART
produces high-quality masks rapidly without additional post-processing and
benefits from co-optimizing the coarse and fine branches.