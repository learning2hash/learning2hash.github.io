---
layout: publication
title: Addressing Challenging Place Recognition Tasks Using Generative Adversarial
  Networks
authors: Yasir Latif, Ravi Garg, Michael Milford, Ian Reid
conference: 2018 IEEE International Conference on Robotics and Automation (ICRA)
year: 2018
bibkey: latif2017addressing
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.08810'}]
tags: ["ICRA", "Robustness"]
short_authors: Latif et al.
---
Place recognition is an essential component of Simultaneous Localization And
Mapping (SLAM). Under severe appearance change, reliable place recognition is a
difficult perception task since the same place is perceptually very different
in the morning, at night, or over different seasons. This work addresses place
recognition as a domain translation task. Using a pair of coupled Generative
Adversarial Networks (GANs), we show that it is possible to generate the
appearance of one domain (such as summer) from another (such as winter) without
requiring image-to-image correspondences across the domains. Mapping between
domains is learned from sets of images in each domain without knowing the
instance-to-instance correspondence by enforcing a cyclic consistency
constraint. In the process, meaningful feature spaces are learned for each
domain, the distances in which can be used for the task of place recognition.
Experiments show that learned features correspond to visual similarity and can
be effectively used for place recognition across seasons.