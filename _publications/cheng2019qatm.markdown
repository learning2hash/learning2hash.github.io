---
layout: publication
title: 'QATM: Quality-aware Template Matching For Deep Learning'
authors: Jiaxin Cheng, Yue Wu, Wael Abd-Almageed, Premkumar Natarajan
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: cheng2019qatm
citations: 75
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.07254'}]
tags: ["CVPR"]
short_authors: Cheng et al.
---
Finding a template in a search image is one of the core problems many
computer vision, such as semantic image semantic, image-to-GPS verification
\etc. We propose a novel quality-aware template matching method, QATM, which is
not only used as a standalone template matching algorithm, but also a trainable
layer that can be easily embedded into any deep neural network. Specifically,
we assess the quality of a matching pair using soft-ranking among all matching
pairs, and thus different matching scenarios such as 1-to-1, 1-to-many, and
many-to-many will be all reflected to different values. Our extensive
evaluation on classic template matching benchmarks and deep learning tasks
demonstrate the effectiveness of QATM. It not only outperforms state-of-the-art
template matching methods when used alone, but also largely improves existing
deep network solutions.