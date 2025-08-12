---
layout: publication
title: Joint Learning Of Hyperbolic Label Embeddings For Hierarchical Multi-label
  Classification
authors: Soumya Chatterjee, Ayush Maheshwari, Ganesh Ramakrishnan, Saketha Nath Jagaralpudi
conference: 'Proceedings of the 16th Conference of the European Chapter of the Association
  for Computational Linguistics: Main Volume'
year: 2021
bibkey: chatterjee2021joint
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.04997'}]
tags: ["Eacl", "Evaluation"]
short_authors: Chatterjee et al.
---
We consider the problem of multi-label classification where the labels lie in
a hierarchy. However, unlike most existing works in hierarchical multi-label
classification, we do not assume that the label-hierarchy is known. Encouraged
by the recent success of hyperbolic embeddings in capturing hierarchical
relations, we propose to jointly learn the classifier parameters as well as the
label embeddings. Such a joint learning is expected to provide a twofold
advantage: i) the classifier generalizes better as it leverages the prior
knowledge of existence of a hierarchy over the labels, and ii) in addition to
the label co-occurrence information, the label-embedding may benefit from the
manifold structure of the input datapoints, leading to embeddings that are more
faithful to the label hierarchy. We propose a novel formulation for the joint
learning and empirically evaluate its efficacy. The results show that the joint
learning improves over the baseline that employs label co-occurrence based
pre-trained hyperbolic embeddings. Moreover, the proposed classifiers achieve
state-of-the-art generalization on standard benchmarks. We also present
evaluation of the hyperbolic embeddings obtained by joint learning and show
that they represent the hierarchy more accurately than the other alternatives.