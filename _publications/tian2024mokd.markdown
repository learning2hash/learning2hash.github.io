---
layout: publication
title: 'MOKD: Cross-domain Finetuning For Few-shot Classification Via Maximizing Optimized
  Kernel Dependence'
authors: Hongduan Tian, Feng Liu, Tongliang Liu, Bo Du, Yiu-Ming Cheung, Bo Han
conference: Arxiv
year: 2024
bibkey: tian2024mokd
citations: 0
additional_links: [{name: Code, url: 'https://github.com/tmlr-group/MOKD\}\{https://github.com/tmlr-group/MOKD\'},
  {name: Paper, url: 'https://arxiv.org/abs/2405.18786'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Tian et al.
---
In cross-domain few-shot classification, *nearest centroid classifier*
(NCC) aims to learn representations to construct a metric space where few-shot
classification can be performed by measuring the similarities between samples
and the prototype of each class. An intuition behind NCC is that each sample is
pulled closer to the class centroid it belongs to while pushed away from those
of other classes. However, in this paper, we find that there exist high
similarities between NCC-learned representations of two samples from different
classes. In order to address this problem, we propose a bi-level optimization
framework, *maximizing optimized kernel dependence* (MOKD) to learn a set
of class-specific representations that match the cluster structures indicated
by labeled data of the given task. Specifically, MOKD first optimizes the
kernel adopted in *Hilbert-Schmidt independence criterion* (HSIC) to
obtain the optimized kernel HSIC (opt-HSIC) that can capture the dependence
more precisely. Then, an optimization problem regarding the opt-HSIC is
addressed to simultaneously maximize the dependence between representations and
labels and minimize the dependence among all samples. Extensive experiments on
Meta-Dataset demonstrate that MOKD can not only achieve better generalization
performance on unseen domains in most cases but also learn better data
representation clusters. The project repository of MOKD is available at:
\href\{https://github.com/tmlr-group/MOKD\}\{https://github.com/tmlr-group/MOKD\}.