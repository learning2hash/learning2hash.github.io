---
layout: publication
title: 'Mssplace: Multi-sensor Place Recognition With Visual And Text Semantics'
authors: Alexander Melekhin, Dmitry Yudin, Ilia Petryashin, Vitaly Bezuglyj
conference: Arxiv
year: 2024
bibkey: melekhin2024mssplace
citations: 0
additional_links: [{name: Code, url: 'https://github.com/alexmelekhin/MSSPlace'},
  {name: Paper, url: 'https://arxiv.org/abs/2407.15663'}]
tags: []
short_authors: Melekhin et al.
---
Place recognition is a challenging task in computer vision, crucial for
enabling autonomous vehicles and robots to navigate previously visited
environments. While significant progress has been made in learnable multimodal
methods that combine onboard camera images and LiDAR point clouds, the full
potential of these methods remains largely unexplored in localization
applications. In this paper, we study the impact of leveraging a multi-camera
setup and integrating diverse data sources for multimodal place recognition,
incorporating explicit visual semantics and text descriptions. Our proposed
method named MSSPlace utilizes images from multiple cameras, LiDAR point
clouds, semantic segmentation masks, and text annotations to generate
comprehensive place descriptors. We employ a late fusion approach to integrate
these modalities, providing a unified representation. Through extensive
experiments on the Oxford RobotCar and NCLT datasets, we systematically analyze
the impact of each data source on the overall quality of place descriptors. Our
experiments demonstrate that combining data from multiple sensors significantly
improves place recognition model performance compared to single modality
approaches and leads to state-of-the-art quality. We also show that separate
usage of visual or textual semantics (which are more compact representations of
sensory data) can achieve promising results in place recognition. The code for
our method is publicly available: https://github.com/alexmelekhin/MSSPlace