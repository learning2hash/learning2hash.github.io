---
layout: publication
title: 'Pit30m: A Benchmark For Global Localization In The Age Of Self-driving Cars'
authors: "Julieta Martinez, Sasha Doubov, Jack Fan, Ioan Andrei B\xE2rsan, Shenlong\
  \ Wang, Gell\xE9rt M\xE1ttyus, Raquel Urtasun"
conference: 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems
  (IROS)
year: 2020
bibkey: martinez2020pit30m
citations: 1
additional_links: [{name: Other, url: 'https://pit30m.github.io/'}, {name: Paper,
    url: 'https://arxiv.org/abs/2012.12437'}]
tags: ["Datasets", "Evaluation"]
short_authors: Martinez et al.
---
We are interested in understanding whether retrieval-based localization
approaches are good enough in the context of self-driving vehicles. Towards
this goal, we introduce Pit30M, a new image and LiDAR dataset with over 30
million frames, which is 10 to 100 times larger than those used in previous
work. Pit30M is captured under diverse conditions (i.e., season, weather, time
of the day, traffic), and provides accurate localization ground truth. We also
automatically annotate our dataset with historical weather and astronomical
data, as well as with image and LiDAR semantic segmentation as a proxy measure
for occlusion. We benchmark multiple existing methods for image and LiDAR
retrieval and, in the process, introduce a simple, yet effective convolutional
network-based LiDAR retrieval method that is competitive with the state of the
art. Our work provides, for the first time, a benchmark for sub-metre
retrieval-based localization at city scale. The dataset, its Python SDK, as
well as more information about the sensors, calibration, and metadata, are
available on the project website: https://pit30m.github.io/