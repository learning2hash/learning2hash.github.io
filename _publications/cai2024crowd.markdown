---
layout: publication
title: 'Crowd-sam: SAM As A Smart Annotator For Object Detection In Crowded Scenes'
authors: Zhi Cai, Yingjie Gao, Yaoyan Zheng, Nan Zhou, di Huang
conference: Lecture Notes in Computer Science
year: 2024
bibkey: cai2024crowd
citations: 3
additional_links: [{name: Code, url: 'https://github.com/FelixCaae/CrowdSAM'}, {name: Paper,
    url: 'https://arxiv.org/abs/2407.11464'}]
tags: ["Efficiency", "Tools & Libraries"]
short_authors: Cai et al.
---
In computer vision, object detection is an important task that finds its
application in many scenarios. However, obtaining extensive labels can be
challenging, especially in crowded scenes. Recently, the Segment Anything Model
(SAM) has been proposed as a powerful zero-shot segmenter, offering a novel
approach to instance segmentation tasks. However, the accuracy and efficiency
of SAM and its variants are often compromised when handling objects in crowded
and occluded scenes. In this paper, we introduce Crowd-SAM, a SAM-based
framework designed to enhance SAM's performance in crowded and occluded scenes
with the cost of few learnable parameters and minimal labeled images. We
introduce an efficient prompt sampler (EPS) and a part-whole discrimination
network (PWD-Net), enhancing mask selection and accuracy in crowded scenes.
Despite its simplicity, Crowd-SAM rivals state-of-the-art (SOTA)
fully-supervised object detection methods on several benchmarks including
CrowdHuman and CityPersons. Our code is available at
https://github.com/FelixCaae/CrowdSAM.