---
layout: publication
title: Progressive Local Filter Pruning For Image Retrieval Acceleration
authors: Xiaodong Wang, Zhedong Zheng, Yang He, Fei Yan, Zhiqiang Zeng, Yi Yang
conference: IEEE Transactions on Multimedia
year: 2023
bibkey: wang2020progressive
citations: 50
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.08878'}]
tags: ["Image Retrieval"]
short_authors: Wang et al.
---
This paper focuses on network pruning for image retrieval acceleration.
Prevailing image retrieval works target at the discriminative feature learning,
while little attention is paid to how to accelerate the model inference, which
should be taken into consideration in real-world practice. The challenge of
pruning image retrieval models is that the middle-level feature should be
preserved as much as possible. Such different requirements of the retrieval and
classification model make the traditional pruning methods not that suitable for
our task. To solve the problem, we propose a new Progressive Local Filter
Pruning (PLFP) method for image retrieval acceleration. Specifically, layer by
layer, we analyze the local geometric properties of each filter and select the
one that can be replaced by the neighbors. Then we progressively prune the
filter by gradually changing the filter weights. In this way, the
representation ability of the model is preserved. To verify this, we evaluate
our method on two widely-used image retrieval datasets,i.e., Oxford5k and
Paris6K, and one person re-identification dataset,i.e., Market-1501. The
proposed method arrives with superior performance to the conventional pruning
methods, suggesting the effectiveness of the proposed method for image
retrieval.