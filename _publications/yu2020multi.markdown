---
layout: publication
title: Multi-layer Feature Aggregation For Deep Scene Parsing Models
authors: Litao Yu, Yongsheng Gao, Jun Zhou, Jian Zhang, Qiang Wu
conference: Arxiv
year: 2020
bibkey: yu2020multi
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.02572'}]
tags: []
short_authors: Yu et al.
---
Scene parsing from images is a fundamental yet challenging problem in visual
content understanding. In this dense prediction task, the parsing model assigns
every pixel to a categorical label, which requires the contextual information
of adjacent image patches. So the challenge for this learning task is to
simultaneously describe the geometric and semantic properties of objects or a
scene. In this paper, we explore the effective use of multi-layer feature
outputs of the deep parsing networks for spatial-semantic consistency by
designing a novel feature aggregation module to generate the appropriate global
representation prior, to improve the discriminative power of features. The
proposed module can auto-select the intermediate visual features to correlate
the spatial and semantic information. At the same time, the multiple skip
connections form a strong supervision, making the deep parsing network easy to
train. Extensive experiments on four public scene parsing datasets prove that
the deep parsing network equipped with the proposed feature aggregation module
can achieve very promising results.