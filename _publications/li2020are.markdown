---
layout: publication
title: Are Fewer Labels Possible For Few-shot Learning?
authors: Suichan Li, Dongdong Chen, Yinpeng Chen, Lu Yuan, Lei Zhang, Qi Chu, Nenghai
  Yu
conference: Arxiv
year: 2020
bibkey: li2020are
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.05899'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Li et al.
---
Few-shot learning is challenging due to its very limited data and labels.
Recent studies in big transfer (BiT) show that few-shot learning can greatly
benefit from pretraining on large scale labeled dataset in a different domain.
This paper asks a more challenging question: "can we use as few as possible
labels for few-shot learning in both pretraining (with no labels) and
fine-tuning (with fewer labels)?".
  Our key insight is that the clustering of target samples in the feature space
is all we need for few-shot finetuning. It explains why the vanilla
unsupervised pretraining (poor clustering) is worse than the supervised one. In
this paper, we propose transductive unsupervised pretraining that achieves a
better clustering by involving target data even though its amount is very
limited. The improved clustering result is of great value for identifying the
most representative samples ("eigen-samples") for users to label, and in
return, continued finetuning with the labeled eigen-samples further improves
the clustering. Thus, we propose eigen-finetuning to enable fewer shot learning
by leveraging the co-evolution of clustering and eigen-samples in the
finetuning. We conduct experiments on 10 different few-shot target datasets,
and our average few-shot performance outperforms both vanilla inductive
unsupervised transfer and supervised transfer by a large margin. For instance,
when each target category only has 10 labeled samples, the mean accuracy gain
over the above two baselines is 9.2% and 3.42 respectively.