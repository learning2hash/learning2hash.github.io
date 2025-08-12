---
layout: publication
title: Query-augmented Active Metric Learning
authors: Yujia Deng, Yubai Yuan, Haoda Fu, Annie Qu
conference: Journal of the American Statistical Association
year: 2021
bibkey: deng2021query
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.04871'}]
tags: ["Distance Metric Learning"]
short_authors: Deng et al.
---
In this paper we propose an active metric learning method for clustering with
pairwise constraints. The proposed method actively queries the label of
informative instance pairs, while estimating underlying metrics by
incorporating unlabeled instance pairs, which leads to a more accurate and
efficient clustering process. In particular, we augment the queried constraints
by generating more pairwise labels to provide additional information in
learning a metric to enhance clustering performance. Furthermore, we increase
the robustness of metric learning by updating the learned metric sequentially
and penalizing the irrelevant features adaptively. In addition, we propose a
novel active query strategy that evaluates the information gain of instance
pairs more accurately by incorporating the neighborhood structure, which
improves clustering efficiency without extra labeling cost. In theory, we
provide a tighter error bound of the proposed metric learning method utilizing
augmented queries compared with methods using existing constraints only.
Furthermore, we also investigate the improvement using the active query
strategy instead of random selection. Numerical studies on simulation settings
and real datasets indicate that the proposed method is especially advantageous
when the signal-to-noise ratio between significant features and irrelevant
features is low.