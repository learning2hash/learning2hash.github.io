---
layout: publication
title: 'Rethinking The Optimization Of Average Precision: Only Penalizing Negative
  Instances Before Positive Ones Is Enough'
authors: Zhuo Li, Weiqing Min, Jiajun Song, Yaohui Zhu, Liping Kang, Xiaoming Wei,
  Xiaolin Wei, Shuqiang Jiang
conference: Arxiv
year: 2021
bibkey: li2021rethinking
citations: 0
additional_links: [{name: Code, url: 'https://github.com/interestingzhuo/PNPloss'},
  {name: Paper, url: 'https://arxiv.org/abs/2102.04640'}]
tags: ["Datasets", "Evaluation", "Image Retrieval"]
short_authors: Li et al.
---
Optimizing the approximation of Average Precision (AP) has been widely
studied for image retrieval. Limited by the definition of AP, such methods
consider both negative and positive instances ranking before each positive
instance. However, we claim that only penalizing negative instances before
positive ones is enough, because the loss only comes from these negative
instances. To this end, we propose a novel loss, namely Penalizing Negative
instances before Positive ones (PNP), which can directly minimize the number of
negative instances before each positive one. In addition, AP-based methods
adopt a fixed and sub-optimal gradient assignment strategy. Therefore, we
systematically investigate different gradient assignment solutions via
constructing derivative functions of the loss, resulting in PNP-I with
increasing derivative functions and PNP-D with decreasing ones. PNP-I focuses
more on the hard positive instances by assigning larger gradients to them and
tries to make all relevant instances closer. In contrast, PNP-D pays less
attention to such instances and slowly corrects them. For most real-world data,
one class usually contains several local clusters. PNP-I blindly gathers these
clusters while PNP-D keeps them as they were. Therefore, PNP-D is more
superior. Experiments on three standard retrieval datasets show consistent
results with the above analysis. Extensive evaluations demonstrate that PNP-D
achieves the state-of-the-art performance. Code is available at
https://github.com/interestingzhuo/PNPloss