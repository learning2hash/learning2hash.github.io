---
layout: publication
title: Interpretable And Generalizable Person Re-identification With Query-adaptive
  Convolution And Temporal Lifting
authors: Shengcai Liao, Ling Shao
conference: Lecture Notes in Computer Science
year: 2020
bibkey: liao2019interpretable
citations: 121
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.10424'}]
tags: []
short_authors: Shengcai Liao, Ling Shao
---
For person re-identification, existing deep networks often focus on
representation learning. However, without transfer learning, the learned model
is fixed as is, which is not adaptable for handling various unseen scenarios.
In this paper, beyond representation learning, we consider how to formulate
person image matching directly in deep feature maps. We treat image matching as
finding local correspondences in feature maps, and construct query-adaptive
convolution kernels on the fly to achieve local matching. In this way, the
matching process and results are interpretable, and this explicit matching is
more generalizable than representation features to unseen scenarios, such as
unknown misalignments, pose or viewpoint changes. To facilitate end-to-end
training of this architecture, we further build a class memory module to cache
feature maps of the most recent samples of each class, so as to compute image
matching losses for metric learning. Through direct cross-dataset evaluation,
the proposed Query-Adaptive Convolution (QAConv) method gains large
improvements over popular learning methods (about 10%+ mAP), and achieves
comparable results to many transfer learning methods. Besides, a model-free
temporal cooccurrence based score weighting method called TLift is proposed,
which improves the performance to a further extent, achieving state-of-the-art
results in cross-dataset person re-identification. Code is available at
https://github.com/ShengcaiLiao/QAConv.