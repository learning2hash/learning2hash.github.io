---
layout: publication
title: 'Deeptag: A General Framework For Fiducial Marker Design And Detection'
authors: Zhuming Zhang, Yongtao Hu, Guoxing Yu, Jingwen Dai
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2022
bibkey: zhang2021deeptag
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.13731'}]
tags: []
short_authors: Zhang et al.
---
A fiducial marker system usually consists of markers, a detection algorithm,
and a coding system. The appearance of markers and the detection robustness are
generally limited by the existing detection algorithms, which are hand-crafted
with traditional low-level image processing techniques. Furthermore, a
sophisticatedly designed coding system is required to overcome the shortcomings
of both markers and detection algorithms. To improve the flexibility and
robustness in various applications, we propose a general deep learning based
framework, DeepTag, for fiducial marker design and detection. DeepTag not only
supports detection of a wide variety of existing marker families, but also
makes it possible to design new marker families with customized local patterns.
Moreover, we propose an effective procedure to synthesize training data on the
fly without manual annotations. Thus, DeepTag can easily adapt to existing and
newly-designed marker families. To validate DeepTag and existing methods,
beside existing datasets, we further collect a new large and challenging
dataset where markers are placed in different view distances and angles.
Experiments show that DeepTag well supports different marker families and
greatly outperforms the existing methods in terms of both detection robustness
and pose accuracy. Both code and dataset are available at
https://herohuyongtao.github.io/research/publications/deep-tag/.