---
layout: publication
title: Metric Learning For Anti-compression Facial Forgery Detection
authors: Shenhao Cao, Qin Zou, Xiuqing Mao, Zhongyuan Wang
conference: Proceedings of the 29th ACM International Conference on Multimedia
year: 2021
bibkey: cao2021metric
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.08397'}]
tags: ["Distance Metric Learning", "Robustness"]
short_authors: Cao et al.
---
Detecting facial forgery images and videos is an increasingly important topic
in multimedia forensics. As forgery images and videos are usually compressed
into different formats such as JPEG and H264 when circulating on the Internet,
existing forgery-detection methods trained on uncompressed data often suffer
from significant performance degradation in identifying them. To solve this
problem, we propose a novel anti-compression facial forgery detection
framework, which learns a compression-insensitive embedding feature space
utilizing both original and compressed forgeries. Specifically, our approach
consists of three ideas: (i) extracting compression-insensitive features from
both uncompressed and compressed forgeries using an adversarial learning
strategy; (ii) learning a robust partition by constructing a metric loss that
can reduce the distance of the paired original and compressed images in the
embedding space; (iii) improving the accuracy of tampered localization with an
attention-transfer module. Experimental results demonstrate that, the proposed
method is highly effective in handling both compressed and uncompressed facial
forgery images.