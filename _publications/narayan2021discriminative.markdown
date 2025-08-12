---
layout: publication
title: Discriminative Region-based Multi-label Zero-shot Learning
authors: Sanath Narayan, Akshita Gupta, Salman Khan, Fahad Shahbaz Khan, Ling Shao,
  Mubarak Shah
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: narayan2021discriminative
citations: 31
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.09301'}]
tags: ["ICCV"]
short_authors: Narayan et al.
---
Multi-label zero-shot learning (ZSL) is a more realistic counter-part of
standard single-label ZSL since several objects can co-exist in a natural
image. However, the occurrence of multiple objects complicates the reasoning
and requires region-specific processing of visual features to preserve their
contextual cues. We note that the best existing multi-label ZSL method takes a
shared approach towards attending to region features with a common set of
attention maps for all the classes. Such shared maps lead to diffused
attention, which does not discriminatively focus on relevant locations when the
number of classes are large. Moreover, mapping spatially-pooled visual features
to the class semantics leads to inter-class feature entanglement, thus
hampering the classification. Here, we propose an alternate approach towards
region-based discriminability-preserving multi-label zero-shot classification.
Our approach maintains the spatial resolution to preserve region-level
characteristics and utilizes a bi-level attention module (BiAM) to enrich the
features by incorporating both region and scene context information. The
enriched region-level features are then mapped to the class semantics and only
their class predictions are spatially pooled to obtain image-level predictions,
thereby keeping the multi-class features disentangled. Our approach sets a new
state of the art on two large-scale multi-label zero-shot benchmarks: NUS-WIDE
and Open Images. On NUS-WIDE, our approach achieves an absolute gain of 6.9%
mAP for ZSL, compared to the best published results.