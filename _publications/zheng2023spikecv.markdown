---
layout: publication
title: 'Spikecv: Open A Continuous Computer Vision Era'
authors: Yajing Zheng, Jiyuan Zhang, Rui Zhao, Jianhao Ding, Shiyan Chen, Ruiqin Xiong,
  Zhaofei Yu, Tiejun Huang
conference: Arxiv
year: 2023
bibkey: zheng2023spikecv
citations: 3
additional_links: [{name: Code, url: 'https://openi.pcl.ac.cn/Cordium/SpikeCV'}, {
    name: Code, url: 'https://github.com/Zyj061/SpikeCV'}, {name: Paper, url: 'https://arxiv.org/abs/2303.11684'}]
tags: []
short_authors: Zheng et al.
---
SpikeCV is a new open-source computer vision platform for the spike camera,
which is a neuromorphic visual sensor that has developed rapidly in recent
years. In the spike camera, each pixel position directly accumulates the light
intensity and asynchronously fires spikes. The output binary spikes can reach a
frequency of 40,000 Hz. As a new type of visual expression, spike sequence has
high spatiotemporal completeness and preserves the continuous visual
information of the external world. Taking advantage of the low latency and high
dynamic range of the spike camera, many spike-based algorithms have made
significant progress, such as high-quality imaging and ultra-high-speed target
detection.
  To build up a community ecology for the spike vision to facilitate more users
to take advantage of the spike camera, SpikeCV provides a variety of
ultra-high-speed scene datasets, hardware interfaces, and an easy-to-use
modules library. SpikeCV focuses on encapsulation for spike data,
standardization for dataset interfaces, modularization for vision tasks, and
real-time applications for challenging scenes. With the advent of the
open-source Python ecosystem, modules of SpikeCV can be used as a Python
library to fulfilled most of the numerical analysis needs of researchers. We
demonstrate the efficiency of the SpikeCV on offline inference and real-time
applications. The project repository address are
https://openi.pcl.ac.cn/Cordium/SpikeCV and
\url\{https://github.com/Zyj061/SpikeCV