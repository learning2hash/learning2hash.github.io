---
layout: publication
title: Quadruplet Network With One-shot Learning For Fast Visual Object Tracking
authors: Xingping Dong, Jianbing Shen, Dongming Wu, Kan Guo, Xiaogang Jin, Fatih Porikli
conference: IEEE Transactions on Image Processing
year: 2019
bibkey: dong2017quadruplet
citations: 173
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.07222'}]
tags: ["Distance Metric Learning", "Efficiency", "Evaluation"]
short_authors: Dong et al.
---
In the same vein of discriminative one-shot learning, Siamese networks allow
recognizing an object from a single exemplar with the same class label.
However, they do not take advantage of the underlying structure of the data and
the relationship among the multitude of samples as they only rely on pairs of
instances for training. In this paper, we propose a new quadruplet deep network
to examine the potential connections among the training instances, aiming to
achieve a more powerful representation. We design four shared networks that
receive multi-tuple of instances as inputs and are connected by a novel loss
function consisting of pair-loss and triplet-loss. According to the similarity
metric, we select the most similar and the most dissimilar instances as the
positive and negative inputs of triplet loss from each multi-tuple. We show
that this scheme improves the training performance. Furthermore, we introduce a
new weight layer to automatically select suitable combination weights, which
will avoid the conflict between triplet and pair loss leading to worse
performance. We evaluate our quadruplet framework by model-free
tracking-by-detection of objects from a single initial exemplar in several
Visual Object Tracking benchmarks. Our extensive experimental analysis
demonstrates that our tracker achieves superior performance with a real-time
processing speed of 78 frames-per-second (fps).