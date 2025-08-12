---
layout: publication
title: Dual-path Frequency Discriminators For Few-shot Anomaly Detection
authors: Yuhu Bai, Jiangning Zhang, Zhaofeng Chen, Yuhang Dong, Yunkang Cao, Guanzhong
  Tian
conference: Arxiv
year: 2024
bibkey: bai2024dual
citations: 1
additional_links: [{name: Code, url: 'https://github.com/yuhbai/DFD'}, {name: Paper,
    url: 'https://arxiv.org/abs/2403.04151'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Bai et al.
---
Few-shot anomaly detection (FSAD) plays a crucial role in industrial
manufacturing. However, existing FSAD methods encounter difficulties leveraging
a limited number of normal samples, frequently failing to detect and locate
inconspicuous anomalies in the spatial domain. We have further discovered that
these subtle anomalies would be more noticeable in the frequency domain. In
this paper, we propose a Dual-Path Frequency Discriminators (DFD) network from
a frequency perspective to tackle these issues. The original spatial images are
transformed into multi-frequency images, making them more conducive to the
tailored discriminators in detecting anomalies. Additionally, the
discriminators learn a joint representation with forms of pseudo-anomalies.
Extensive experiments conducted on MVTec AD and VisA benchmarks demonstrate
that our DFD surpasses current state-of-the-art methods. The code is available
at https://github.com/yuhbai/DFD.