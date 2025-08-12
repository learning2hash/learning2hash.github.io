---
layout: publication
title: Variational Feature Disentangling For Fine-grained Few-shot Classification
authors: Jingyi Xu, Hieu Le, Mingzhen Huang, Shahrukh Athar, Dimitris Samaras
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: xu2020variational
citations: 50
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.03255'}]
tags: ["Few Shot & Zero Shot", "ICCV"]
short_authors: Xu et al.
---
Fine-grained few-shot recognition often suffers from the problem of training
data scarcity for novel categories.The network tends to overfit and does not
generalize well to unseen classes due to insufficient training data. Many
methods have been proposed to synthesize additional data to support the
training. In this paper, we focus one enlarging the intra-class variance of the
unseen class to improve few-shot classification performance. We assume that the
distribution of intra-class variance generalizes across the base class and the
novel class. Thus, the intra-class variance of the base set can be transferred
to the novel set for feature augmentation. Specifically, we first model the
distribution of intra-class variance on the base set via variational inference.
Then the learned distribution is transferred to the novel set to generate
additional features, which are used together with the original ones to train a
classifier. Experimental results show a significant boost over the
state-of-the-art methods on the challenging fine-grained few-shot image
classification benchmarks.