---
layout: publication
title: 'If-net: An Illumination-invariant Feature Network'
authors: Po-Heng Chen, Zhao-Xu Luo, Zu-Kuan Huang, Chun Yang, Kuan-Wen Chen
conference: 2020 IEEE International Conference on Robotics and Automation (ICRA)
year: 2020
bibkey: chen2020if
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.03897'}]
tags: [Evaluation, ICRA, Datasets, Image Retrieval]
short_authors: Chen et al.
---
Feature descriptor matching is a critical step is many computer vision
applications such as image stitching, image retrieval and visual localization.
However, it is often affected by many practical factors which will degrade its
performance. Among these factors, illumination variations are the most
influential one, and especially no previous descriptor learning works focus on
dealing with this problem. In this paper, we propose IF-Net, aimed to generate
a robust and generic descriptor under crucial illumination changes conditions.
We find out not only the kind of training data important but also the order it
is presented. To this end, we investigate several dataset scheduling methods
and propose a separation training scheme to improve the matching accuracy.
Further, we propose a ROI loss and hard-positive mining strategy along with the
training scheme, which can strengthen the ability of generated descriptor
dealing with large illumination change conditions. We evaluate our approach on
public patch matching benchmark and achieve the best results compared with
several state-of-the-arts methods. To show the practicality, we further
evaluate IF-Net on the task of visual localization under large illumination
changes scenes, and achieves the best localization accuracy.