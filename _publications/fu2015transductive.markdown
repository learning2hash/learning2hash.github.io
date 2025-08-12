---
layout: publication
title: Transductive Multi-view Zero-shot Learning
authors: Yanwei Fu, Timothy M. Hospedales, Tao Xiang, Shaogang Gong
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2015
bibkey: fu2015transductive
citations: 521
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1501.04560'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Fu et al.
---
Most existing zero-shot learning approaches exploit transfer learning via an
intermediate-level semantic representation shared between an annotated
auxiliary dataset and a target dataset with different classes and no
annotation. A projection from a low-level feature space to the semantic
representation space is learned from the auxiliary dataset and is applied
without adaptation to the target dataset. In this paper we identify two
inherent limitations with these approaches. First, due to having disjoint and
potentially unrelated classes, the projection functions learned from the
auxiliary dataset/domain are biased when applied directly to the target
dataset/domain. We call this problem the projection domain shift problem and
propose a novel framework, transductive multi-view embedding, to solve it. The
second limitation is the prototype sparsity problem which refers to the fact
that for each target class, only a single prototype is available for zero-shot
learning given a semantic representation. To overcome this problem, a novel
heterogeneous multi-view hypergraph label propagation method is formulated for
zero-shot learning in the transductive embedding space. It effectively exploits
the complementary information offered by different semantic representations and
takes advantage of the manifold structures of multiple representation spaces in
a coherent manner. We demonstrate through extensive experiments that the
proposed approach (1) rectifies the projection shift between the auxiliary and
target domains, (2) exploits the complementarity of multiple semantic
representations, (3) significantly outperforms existing methods for both
zero-shot and N-shot recognition on three image and video benchmark datasets,
and (4) enables novel cross-view annotation tasks.