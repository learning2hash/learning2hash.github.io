---
layout: publication
title: Exploring Visual Context For Weakly Supervised Person Search
authors: Yichao Yan, Jinpeng Li, Shengcai Liao, Jie Qin, Bingbing Ni, Xiaokang Yang,
  Ling Shao
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2022
bibkey: yan2021exploring
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.10506'}]
tags: ["AAAI"]
short_authors: Yan et al.
---
Person search has recently emerged as a challenging task that jointly
addresses pedestrian detection and person re-identification. Existing
approaches follow a fully supervised setting where both bounding box and
identity annotations are available. However, annotating identities is
labor-intensive, limiting the practicability and scalability of current
frameworks. This paper inventively considers weakly supervised person search
with only bounding box annotations. We proposed to address this novel task by
investigating three levels of context clues (i.e., detection, memory and scene)
in unconstrained natural images. The first two are employed to promote local
and global discriminative capabilities, while the latter enhances clustering
accuracy. Despite its simple design, our CGPS achieves 80.0% in mAP on
CUHK-SYSU, boosting the baseline model by 8.8%. Surprisingly, it even achieves
comparable performance with several supervised person search models. Our code
is available at https://github.com/ljpadam/CGPS