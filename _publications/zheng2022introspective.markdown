---
layout: publication
title: Introspective Deep Metric Learning For Image Retrieval
authors: Zheng Wenzhao, Wang Chengkun, Zhou Jie, Lu Jiwen
conference: Arxiv
year: 2022
bibkey: zheng2022introspective
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.04449'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Image Retrieval"]
short_authors: Zheng et al.
---
This paper proposes an introspective deep metric learning (IDML) framework
for uncertainty-aware comparisons of images. Conventional deep metric learning
methods produce confident semantic distances between images regardless of the
uncertainty level. However, we argue that a good similarity model should
consider the semantic discrepancies with caution to better deal with ambiguous
images for more robust training. To achieve this, we propose to represent an
image using not only a semantic embedding but also an accompanying uncertainty
embedding, which describes the semantic characteristics and ambiguity of an
image, respectively. We further propose an introspective similarity metric to
make similarity judgments between images considering both their semantic
differences and ambiguities. The proposed IDML framework improves the
performance of deep metric learning through uncertainty modeling and attains
state-of-the-art results on the widely used CUB-200-2011, Cars196, and Stanford
Online Products datasets for image retrieval and clustering. We further provide
an in-depth analysis of our framework to demonstrate the effectiveness and
reliability of IDML. Code is available at: https://github.com/wzzheng/IDML.