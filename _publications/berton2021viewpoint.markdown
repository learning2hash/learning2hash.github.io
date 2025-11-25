---
layout: publication
title: Viewpoint Invariant Dense Matching For Visual Geolocalization
authors: Gabriele Berton, Carlo Masone, Valerio Paolicelli, Barbara Caputo
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: berton2021viewpoint
citations: 31
additional_links: [{name: Code, url: 'https://github.com/gmberton/geo_warp'}, {name: Paper,
    url: 'https://arxiv.org/abs/2109.09827'}]
tags: ["ICCV", "Re-Ranking", "Self-Supervised"]
short_authors: Berton et al.
---
In this paper we propose a novel method for image matching based on dense
local features and tailored for visual geolocalization. Dense local features
matching is robust against changes in illumination and occlusions, but not
against viewpoint shifts which are a fundamental aspect of geolocalization. Our
method, called GeoWarp, directly embeds invariance to viewpoint shifts in the
process of extracting dense features. This is achieved via a trainable module
which learns from the data an invariance that is meaningful for the task of
recognizing places. We also devise a new self-supervised loss and two new
weakly supervised losses to train this module using only unlabeled data and
weak labels. GeoWarp is implemented efficiently as a re-ranking method that can
be easily embedded into pre-existing visual geolocalization pipelines.
Experimental validation on standard geolocalization benchmarks demonstrates
that GeoWarp boosts the accuracy of state-of-the-art retrieval architectures.
The code and trained models are available at
https://github.com/gmberton/geo_warp