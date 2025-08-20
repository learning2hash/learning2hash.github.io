---
layout: publication
title: Deep Dense Local Feature Matching And Vehicle Removal For Indoor Visual Localization
authors: Kyung Ho Park
conference: Arxiv
year: 2022
bibkey: park2022deep
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.12544'}]
tags: [Tools & Libraries, Datasets, Evaluation]
short_authors: Kyung Ho Park
---
Visual localization is an essential component of intelligent transportation
systems, enabling broad applications that require understanding one's self
location when other sensors are not available. It is mostly tackled by image
retrieval such that the location of a query image is determined by its closest
match in the previously collected images. Existing approaches focus on large
scale localization where landmarks are helpful in finding the location.
However, visual localization becomes challenging in small scale environments
where objects are hardly recognizable. In this paper, we propose a visual
localization framework that robustly finds the match for a query among the
images collected from indoor parking lots. It is a challenging problem when the
vehicles in the images share similar appearances and are frequently replaced
such as parking lots. We propose to employ a deep dense local feature matching
that resembles human perception to find correspondences and eliminating matches
from vehicles automatically with a vehicle detector. The proposed solution is
robust to the scenes with low textures and invariant to false matches caused by
vehicles. We compare our framework with alternatives to validate our
superiority on a benchmark dataset containing 267 pre-collected images and 99
query images taken from 34 sections of a parking lot. Our method achieves 86.9
percent accuracy, outperforming the alternatives.