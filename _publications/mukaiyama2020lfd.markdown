---
layout: publication
title: 'Lfd-protonet: Prototypical Network Based On Local Fisher Discriminant Analysis
  For Few-shot Learning'
authors: Kei Mukaiyama, Issei Sato, Masashi Sugiyama
conference: Arxiv
year: 2020
bibkey: mukaiyama2020lfd
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.08306'}]
tags: ["Distance Metric Learning"]
short_authors: Kei Mukaiyama, Issei Sato, Masashi Sugiyama
---
The prototypical network (ProtoNet) is a few-shot learning framework that
performs metric learning and classification using the distance to prototype
representations of each class. It has attracted a great deal of attention
recently since it is simple to implement, highly extensible, and performs well
in experiments. However, it only takes into account the mean of the support
vectors as prototypes and thus it performs poorly when the support set has high
variance. In this paper, we propose to combine ProtoNet with local Fisher
discriminant analysis to reduce the local within-class covariance and increase
the local between-class covariance of the support set. We show the usefulness
of the proposed method by theoretically providing an expected risk bound and
empirically demonstrating its superior classification accuracy on miniImageNet
and tieredImageNet.