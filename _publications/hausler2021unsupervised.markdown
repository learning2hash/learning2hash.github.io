---
layout: publication
title: Unsupervised Complementary-aware Multi-process Fusion For Visual Place Recognition
authors: Stephen Hausler, Tobias Fischer, Michael Milford
conference: Arxiv
year: 2021
bibkey: hausler2021unsupervised
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.04701'}]
tags: ["Datasets", "Evaluation", "Supervised", "Unsupervised"]
short_authors: Stephen Hausler, Tobias Fischer, Michael Milford
---
A recent approach to the Visual Place Recognition (VPR) problem has been to
fuse the place recognition estimates of multiple complementary VPR techniques
simultaneously. However, selecting the optimal set of techniques to use in a
specific deployment environment a-priori is a difficult and unresolved
challenge. Further, to the best of our knowledge, no method exists which can
select a set of techniques on a frame-by-frame basis in response to
image-to-image variations. In this work, we propose an unsupervised algorithm
that finds the most robust set of VPR techniques to use in the current
deployment environment, on a frame-by-frame basis. The selection of techniques
is determined by an analysis of the similarity scores between the current query
image and the collection of database images and does not require ground-truth
information. We demonstrate our approach on a wide variety of datasets and VPR
techniques and show that the proposed dynamic multi-process fusion (Dyn-MPF)
has superior VPR performance compared to a variety of challenging competitive
methods, some of which are given an unfair advantage through access to the
ground-truth information.