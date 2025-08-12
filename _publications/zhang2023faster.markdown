---
layout: publication
title: 'Faster Orefsdet : A Lightweight And Effective Few-shot Object Detector For
  Ore Images'
authors: Yang Zhang, Le Cheng, Yuting Peng, Chengming Xu, Yanwei Fu, Bo Wu, Guodong
  Sun
conference: Pattern Recognition
year: 2023
bibkey: zhang2023faster
citations: 6
additional_links: [{name: Code, url: 'https://github.com/MVME-HBUT/Faster-OreFSDet'},
  {name: Paper, url: 'https://arxiv.org/abs/2305.01183'}]
tags: ["Evaluation", "Few Shot & Zero Shot"]
short_authors: Zhang et al.
---
For the ore particle size detection, obtaining a sizable amount of
high-quality ore labeled data is time-consuming and expensive. General object
detection methods often suffer from severe over-fitting with scarce labeled
data. Despite their ability to eliminate over-fitting, existing few-shot object
detectors encounter drawbacks such as slow detection speed and high memory
requirements, making them difficult to implement in a real-world deployment
scenario. To this end, we propose a lightweight and effective few-shot detector
to achieve competitive performance with general object detection with only a
few samples for ore images. First, the proposed support feature mining block
characterizes the importance of location information in support features. Next,
the relationship guidance block makes full use of support features to guide the
generation of accurate candidate proposals. Finally, the dual-scale semantic
aggregation module retrieves detailed features at different resolutions to
contribute with the prediction process. Experimental results show that our
method consistently exceeds the few-shot detectors with an excellent
performance gap on all metrics. Moreover, our method achieves the smallest
model size of 19MB as well as being competitive at 50 FPS detection speed
compared with general object detectors. The source code is available at
https://github.com/MVME-HBUT/Faster-OreFSDet.