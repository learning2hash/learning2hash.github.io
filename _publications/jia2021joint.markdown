---
layout: publication
title: Joint Representation Learning And Novel Category Discovery On Single- And Multi-modal
  Data
authors: Xuhui Jia, Kai Han, Yukun Zhu, Bradley Green
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: jia2021joint
citations: 46
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.12673'}]
tags: ["Hashing Methods", "ICCV", "Scalability", "Self-Supervised", "Supervised", "Tools & Libraries"]
short_authors: Jia et al.
---
This paper studies the problem of novel category discovery on single- and
multi-modal data with labels from different but relevant categories. We present
a generic, end-to-end framework to jointly learn a reliable representation and
assign clusters to unlabelled data. To avoid over-fitting the learnt embedding
to labelled data, we take inspiration from self-supervised representation
learning by noise-contrastive estimation and extend it to jointly handle
labelled and unlabelled data. In particular, we propose using category
discrimination on labelled data and cross-modal discrimination on multi-modal
data to augment instance discrimination used in conventional contrastive
learning approaches. We further employ Winner-Take-All (WTA) hashing algorithm
on the shared representation space to generate pairwise pseudo labels for
unlabelled data to better predict cluster assignments. We thoroughly evaluate
our framework on large-scale multi-modal video benchmarks Kinetics-400 and
VGG-Sound, and image benchmarks CIFAR10, CIFAR100 and ImageNet, obtaining
state-of-the-art results.