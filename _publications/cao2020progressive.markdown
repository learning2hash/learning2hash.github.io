---
layout: publication
title: Progressive Bilateral-context Driven Model For Post-processing Person Re-identification
authors: Min Cao, Chen Chen, Hao Dou, Xiyuan Hu, Silong Peng, Arjan Kuijper
conference: IEEE Transactions on Multimedia
year: 2020
bibkey: cao2020progressive
citations: 13
additional_links: [{name: Code, url: 'https://github.com/123ci/PBCmodel'}, {name: Paper,
    url: 'https://arxiv.org/abs/2009.03098'}]
tags: []
short_authors: Cao et al.
---
Most existing person re-identification methods compute pairwise similarity by
extracting robust visual features and learning the discriminative metric. Owing
to visual ambiguities, these content-based methods that determine the pairwise
relationship only based on the similarity between them, inevitably produce a
suboptimal ranking list. Instead, the pairwise similarity can be estimated more
accurately along the geodesic path of the underlying data manifold by exploring
the rich contextual information of the sample. In this paper, we propose a
lightweight post-processing person re-identification method in which the
pairwise measure is determined by the relationship between the sample and the
counterpart's context in an unsupervised way. We translate the point-to-point
comparison into the bilateral point-to-set comparison. The sample's context is
composed of its neighbor samples with two different definition ways: the first
order context and the second order context, which are used to compute the
pairwise similarity in sequence, resulting in a progressive post-processing
model. The experiments on four large-scale person re-identification benchmark
datasets indicate that (1) the proposed method can consistently achieve higher
accuracies by serving as a post-processing procedure after the content-based
person re-identification methods, showing its state-of-the-art results, (2) the
proposed lightweight method only needs about 6 milliseconds for optimizing the
ranking results of one sample, showing its high-efficiency. Code is available
at: https://github.com/123ci/PBCmodel.