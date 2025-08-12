---
layout: publication
title: Disentangled Feature Representation For Few-shot Image Classification
authors: Hao Cheng, Yufei Wang, Haoliang Li, Alex C. Kot, Bihan Wen
conference: IEEE Transactions on Neural Networks and Learning Systems
year: 2023
bibkey: cheng2021disentangled
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.12548'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Cheng et al.
---
Learning the generalizable feature representation is critical for few-shot
image classification. While recent works exploited task-specific feature
embedding using meta-tasks for few-shot learning, they are limited in many
challenging tasks as being distracted by the excursive features such as the
background, domain and style of the image samples. In this work, we propose a
novel Disentangled Feature Representation framework, dubbed DFR, for few-shot
learning applications. DFR can adaptively decouple the discriminative features
that are modeled by the classification branch, from the class-irrelevant
component of the variation branch. In general, most of the popular deep
few-shot learning methods can be plugged in as the classification branch, thus
DFR can boost their performance on various few-shot tasks. Furthermore, we
propose a novel FS-DomainNet dataset based on DomainNet, for benchmarking the
few-shot domain generalization tasks. We conducted extensive experiments to
evaluate the proposed DFR on general and fine-grained few-shot classification,
as well as few-shot domain generalization, using the corresponding four
benchmarks, i.e., mini-ImageNet, tiered-ImageNet, CUB, as well as the proposed
FS-DomainNet. Thanks to the effective feature disentangling, the DFR-based
few-shot classifiers achieved the state-of-the-art results on all datasets.