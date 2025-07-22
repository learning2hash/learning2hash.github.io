---
layout: publication
title: 'GRM: Gradient Rectification Module For Visual Place Retrieval'
authors: Lei Boshu, Ding Wenjie, Qiao Limeng, Qiu Xi
conference: 2023 IEEE International Conference on Robotics and Automation (ICRA)
year: 2023
bibkey: lei2022grm
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.10972'}]
tags: ["Tools-&-Libraries", "Evaluation", "Datasets"]
short_authors: Lei et al.
---
Visual place retrieval aims to search images in the database that depict
similar places as the query image. However, global descriptors encoded by the
network usually fall into a low dimensional principal space, which is harmful
to the retrieval performance. We first analyze the cause of this phenomenon,
pointing out that it is due to degraded distribution of the gradients of
descriptors. Then, we propose Gradient Rectification Module(GRM) to alleviate
this issue. GRM is appended after the final pooling layer and can rectify
gradients to the complementary space of the principal space. With GRM, the
network is encouraged to generate descriptors more uniformly in the whole
space. At last, we conduct experiments on multiple datasets and generalize our
method to classification task under prototype learning framework.