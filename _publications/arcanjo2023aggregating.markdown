---
layout: publication
title: Aggregating Multiple Bio-inspired Image Region Classifiers For Effective And
  Lightweight Visual Place Recognition
authors: Bruno Arcanjo, Bruno Ferrarini, Maria Fasli, Michael Milford, Klaus D. Mcdonald-maier,
  Shoaib Ehsan
conference: IEEE Robotics and Automation Letters
year: 2024
bibkey: arcanjo2023aggregating
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.12995'}]
tags: ["Efficiency"]
short_authors: Arcanjo et al.
---
Visual place recognition (VPR) enables autonomous systems to localize
themselves within an environment using image information. While VPR techniques
built upon a Convolutional Neural Network (CNN) backbone dominate
state-of-the-art VPR performance, their high computational requirements make
them unsuitable for platforms equipped with low-end hardware. Recently, a
lightweight VPR system based on multiple bio-inspired classifiers, dubbed
DrosoNets, has been proposed, achieving great computational efficiency at the
cost of reduced absolute place retrieval performance. In this work, we propose
a novel multi-DrosoNet localization system, dubbed RegionDrosoNet, with
significantly improved VPR performance, while preserving a low-computational
profile. Our approach relies on specializing distinct groups of DrosoNets on
differently sliced partitions of the original image, increasing extrinsic model
differentiation. Furthermore, we introduce a novel voting module to combine the
outputs of all DrosoNets into the final place prediction which considers
multiple top refence candidates from each DrosoNet. RegionDrosoNet outperforms
other lightweight VPR techniques when dealing with both appearance changes and
viewpoint variations. Moreover, it competes with computationally expensive
methods on some benchmark datasets at a small fraction of their online
inference time.