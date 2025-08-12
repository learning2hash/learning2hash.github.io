---
layout: publication
title: 'NOH-NMS: Improving Pedestrian Detection By Nearby Objects Hallucination'
authors: Penghao Zhou, Chong Zhou, Pai Peng, Junlong Du, Xing Sun, Xiaowei Guo, Feiyue
  Huang
conference: Arxiv
year: 2020
bibkey: zhou2020noh
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.13376'}]
tags: []
short_authors: Zhou et al.
---
Greedy-NMS inherently raises a dilemma, where a lower NMS threshold will
potentially lead to a lower recall rate and a higher threshold introduces more
false positives. This problem is more severe in pedestrian detection because
the instance density varies more intensively. However, previous works on NMS
don't consider or vaguely consider the factor of the existent of nearby
pedestrians. Thus, we propose Nearby Objects Hallucinator (NOH), which
pinpoints the objects nearby each proposal with a Gaussian distribution,
together with NOH-NMS, which dynamically eases the suppression for the space
that might contain other objects with a high likelihood. Compared to
Greedy-NMS, our method, as the state-of-the-art, improves by \(3.9%\) AP,
\(5.1%\) Recall, and \(0.8%\) \(\text\{MR\}^\{-2\}\) on CrowdHuman to \(89.0%\) AP and
\(92.9%\) Recall, and \(43.9%\) \(\text\{MR\}^\{-2\}\) respectively.