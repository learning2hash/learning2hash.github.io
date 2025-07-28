---
layout: publication
title: 'NPR: Nocturnal Place Recognition In Streets'
authors: Bingxi Liu, Yujie Fu, Feng Lu, Jinqiang Cui, Yihong Wu, Hong Zhang
conference: Arxiv
year: 2023
bibkey: liu2023npr
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.00276'}]
tags: []
short_authors: Liu et al.
---
Visual Place Recognition (VPR) is the task of retrieving database images
similar to a query photo by comparing it to a large database of known images.
In real-world applications, extreme illumination changes caused by query images
taken at night pose a significant obstacle that VPR needs to overcome. However,
a training set with day-night correspondence for city-scale, street-level VPR
does not exist. To address this challenge, we propose a novel pipeline that
divides VPR and conquers Nocturnal Place Recognition (NPR). Specifically, we
first established a street-level day-night dataset, NightStreet, and used it to
train an unpaired image-to-image translation model. Then we used this model to
process existing large-scale VPR datasets to generate the VPR-Night datasets
and demonstrated how to combine them with two popular VPR pipelines. Finally,
we proposed a divide-and-conquer VPR framework and provided explanations at the
theoretical, experimental, and application levels. Under our framework,
previous methods can significantly improve performance on two public datasets,
including the top-ranked method.