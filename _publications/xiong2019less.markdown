---
layout: publication
title: 'Less Is More: Learning Highlight Detection From Video Duration'
authors: Bo Xiong, Yannis Kalantidis, Deepti Ghadiyaram, Kristen Grauman
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: xiong2019less
citations: 106
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.00859'}]
tags: ["CVPR"]
short_authors: Xiong et al.
---
Highlight detection has the potential to significantly ease video browsing,
but existing methods often suffer from expensive supervision requirements,
where human viewers must manually identify highlights in training videos. We
propose a scalable unsupervised solution that exploits video duration as an
implicit supervision signal. Our key insight is that video segments from
shorter user-generated videos are more likely to be highlights than those from
longer videos, since users tend to be more selective about the content when
capturing shorter videos. Leveraging this insight, we introduce a novel ranking
framework that prefers segments from shorter videos, while properly accounting
for the inherent noise in the (unlabeled) training data. We use it to train a
highlight detector with 10M hashtagged Instagram videos. In experiments on two
challenging public video highlight detection benchmarks, our method
substantially improves the state-of-the-art for unsupervised highlight
detection.