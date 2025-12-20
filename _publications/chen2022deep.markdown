---
layout: publication
title: Deep Multi-view Semi-supervised Clustering With Sample Pairwise Constraints
authors: Rui Chen, Yongqiang Tang, Wensheng Zhang, Wenlong Feng
conference: Neurocomputing
year: 2022
bibkey: chen2022deep
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.04949'}]
tags: ["Datasets", "Evaluation", "Supervised"]
short_authors: Chen et al.
---
Multi-view clustering has attracted much attention thanks to the capacity of
multi-source information integration. Although numerous advanced methods have
been proposed in past decades, most of them generally overlook the significance
of weakly-supervised information and fail to preserve the feature properties of
multiple views, thus resulting in unsatisfactory clustering performance. To
address these issues, in this paper, we propose a novel Deep Multi-view
Semi-supervised Clustering (DMSC) method, which jointly optimizes three kinds
of losses during networks finetuning, including multi-view clustering loss,
semi-supervised pairwise constraint loss and multiple autoencoders
reconstruction loss. Specifically, a KL divergence based multi-view clustering
loss is imposed on the common representation of multi-view data to perform
heterogeneous feature optimization, multi-view weighting and clustering
prediction simultaneously. Then, we innovatively propose to integrate pairwise
constraints into the process of multi-view clustering by enforcing the learned
multi-view representation of must-link samples (cannot-link samples) to be
similar (dissimilar), such that the formed clustering architecture can be more
credible. Moreover, unlike existing rivals that only preserve the encoders for
each heterogeneous branch during networks finetuning, we further propose to
tune the intact autoencoders frame that contains both encoders and decoders. In
this way, the issue of serious corruption of view-specific and view-shared
feature space could be alleviated, making the whole training procedure more
stable. Through comprehensive experiments on eight popular image datasets, we
demonstrate that our proposed approach performs better than the
state-of-the-art multi-view and single-view competitors.