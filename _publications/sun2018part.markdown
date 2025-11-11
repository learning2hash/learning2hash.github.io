---
layout: publication
title: Part-based Multi-stream Model For Vehicle Searching
authors: Ya Sun, Minxian Li, Jianfeng Lu
conference: 2018 24th International Conference on Pattern Recognition (ICPR)
year: 2018
bibkey: sun2018part
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.04144'}]
tags: ["Datasets", "Distance Metric Learning", "Neural Hashing"]
short_authors: Ya Sun, Minxian Li, Jianfeng Lu
---
Due to the enormous requirement in public security and intelligent
transportation system, searching an identical vehicle has become more and more
important. Current studies usually treat vehicle as an integral object and then
train a distance metric to measure the similarity among vehicles. However,
these raw images may be exactly similar to ones with different identification
and include some pixels in background that may disturb the distance metric
learning. In this paper, we propose a novel and useful method to segment an
original vehicle image into several discriminative foreground parts, and these
parts consist of some fine grained regions that are named discriminative
patches. After that, these parts combined with the raw image are fed into the
proposed deep learning network. We can easily measure the similarity of two
vehicle images by computing the Euclidean distance of the features from FC
layer. Two main contributions of this paper are as follows. Firstly, a method
is proposed to estimate if a patch in a raw vehicle image is discriminative or
not. Secondly, a new Part-based Multi-Stream Model (PMSM) is designed and
optimized for vehicle retrieval and re-identification tasks. We evaluate the
proposed method on the VehicleID dataset, and the experimental results show
that our method can outperform the baseline.