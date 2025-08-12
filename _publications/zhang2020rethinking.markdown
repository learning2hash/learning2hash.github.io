---
layout: publication
title: 'Rethinking Class Relations: Absolute-relative Supervised And Unsupervised
  Few-shot Learning'
authors: Hongguang Zhang, Piotr Koniusz, Songlei Jian, Hongdong Li, Philip H. S. Torr
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: zhang2020rethinking
citations: 57
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.03919'}]
tags: ["CVPR", "Supervised", "Unsupervised"]
short_authors: Zhang et al.
---
The majority of existing few-shot learning methods describe image relations
with binary labels. However, such binary relations are insufficient to teach
the network complicated real-world relations, due to the lack of decision
smoothness. Furthermore, current few-shot learning models capture only the
similarity via relation labels, but they are not exposed to class concepts
associated with objects, which is likely detrimental to the classification
performance due to underutilization of the available class labels. To
paraphrase, children learn the concept of tiger from a few of actual examples
as well as from comparisons of tiger to other animals. Thus, we hypothesize
that in fact both similarity and class concept learning must be occurring
simultaneously. With these observations at hand, we study the fundamental
problem of simplistic class modeling in current few-shot learning methods. We
rethink the relations between class concepts, and propose a novel
Absolute-relative Learning paradigm to fully take advantage of label
information to refine the image representations and correct the relation
understanding in both supervised and unsupervised scenarios. Our proposed
paradigm improves the performance of several the state-of-the-art models on
publicly available datasets.