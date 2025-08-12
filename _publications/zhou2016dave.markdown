---
layout: publication
title: 'DAVE: A Unified Framework For Fast Vehicle Detection And Annotation'
authors: Yi Zhou, Li Liu, Ling Shao, Matt Mellor
conference: Lecture Notes in Computer Science
year: 2016
bibkey: zhou2016dave
citations: 76
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1607.04564'}]
tags: ["Tools & Libraries"]
short_authors: Zhou et al.
---
Vehicle detection and annotation for streaming video data with complex scenes
is an interesting but challenging task for urban traffic surveillance. In this
paper, we present a fast framework of Detection and Annotation for Vehicles
(DAVE), which effectively combines vehicle detection and attributes annotation.
DAVE consists of two convolutional neural networks (CNNs): a fast vehicle
proposal network (FVPN) for vehicle-like objects extraction and an attributes
learning network (ALN) aiming to verify each proposal and infer each vehicle's
pose, color and type simultaneously. These two nets are jointly optimized so
that abundant latent knowledge learned from the ALN can be exploited to guide
FVPN training. Once the system is trained, it can achieve efficient vehicle
detection and annotation for real-world traffic surveillance data. We evaluate
DAVE on a new self-collected UTS dataset and the public PASCAL VOC2007 car and
LISA 2010 datasets, with consistent improvements over existing algorithms.