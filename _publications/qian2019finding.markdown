---
layout: publication
title: On Finding Gray Pixels
authors: "Yanlin Qian, Joni-Kristian K\xE4m\xE4r\xE4inen, Jarno Nikkanen, Jiri Matas"
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: qian2019finding
citations: 60
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.03198'}]
tags: ["CVPR"]
short_authors: Qian et al.
---
We propose a novel grayness index for finding gray pixels and demonstrate its
effectiveness and efficiency in illumination estimation. The grayness index, GI
in short, is derived using the Dichromatic Reflection Model and is
learning-free. GI allows to estimate one or multiple illumination sources in
color-biased images. On standard single-illumination and multiple-illumination
estimation benchmarks, GI outperforms state-of-the-art statistical methods and
many recent deep methods. GI is simple and fast, written in a few dozen lines
of code, processing a 1080p image in ~0.4 seconds with a non-optimized Matlab
code.