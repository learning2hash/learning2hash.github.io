---
layout: publication
title: Instance-level Human Parsing Via Part Grouping Network
authors: Ke Gong, Xiaodan Liang, Yicheng Li, Yimin Chen, Ming Yang, Liang Lin
conference: Lecture Notes in Computer Science
year: 2018
bibkey: gong2018instance
citations: 339
additional_links: [{name: Code, url: 'http://sysu-hcp.net/lip/'}, {name: Paper, url: 'https://arxiv.org/abs/1808.00157'}]
tags: []
short_authors: Gong et al.
---
Instance-level human parsing towards real-world human analysis scenarios is
still under-explored due to the absence of sufficient data resources and
technical difficulty in parsing multiple instances in a single pass. Several
related works all follow the "parsing-by-detection" pipeline that heavily
relies on separately trained detection models to localize instances and then
performs human parsing for each instance sequentially. Nonetheless, two
discrepant optimization targets of detection and parsing lead to suboptimal
representation learning and error accumulation for final results. In this work,
we make the first attempt to explore a detection-free Part Grouping Network
(PGN) for efficiently parsing multiple people in an image in a single pass. Our
PGN reformulates instance-level human parsing as two twinned sub-tasks that can
be jointly learned and mutually refined via a unified network: 1) semantic part
segmentation for assigning each pixel as a human part (e.g., face, arms); 2)
instance-aware edge detection to group semantic parts into distinct person
instances. Thus the shared intermediate representation would be endowed with
capabilities in both characterizing fine-grained parts and inferring instance
belongings of each part. Finally, a simple instance partition process is
employed to get final results during inference. We conducted experiments on
PASCAL-Person-Part dataset and our PGN outperforms all state-of-the-art
methods. Furthermore, we show its superiority on a newly collected multi-person
parsing dataset (CIHP) including 38,280 diverse images, which is the largest
dataset so far and can facilitate more advanced human analysis. The CIHP
benchmark and our source code are available at http://sysu-hcp.net/lip/.