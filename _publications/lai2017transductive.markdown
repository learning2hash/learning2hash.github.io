---
layout: publication
title: Transductive Zero-shot Hashing Via Coarse-to-fine Similarity Mining
authors: Lai Hanjiang, Pan Yan
conference: Proceedings of the 2018 ACM on International Conference on Multimedia
  Retrieval
year: 2018
bibkey: lai2017transductive
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.02856'}]
tags: ["Datasets", "Evaluation", "Hashing-Methods", "Multimodal-Retrieval", "Few-Shot-&-Zero-Shot"]
short_authors: Lai Hanjiang, Pan Yan
---
Zero-shot Hashing (ZSH) is to learn hashing models for novel/target classes
without training data, which is an important and challenging problem. Most
existing ZSH approaches exploit transfer learning via an intermediate shared
semantic representations between the seen/source classes and novel/target
classes. However, due to having disjoint, the hash functions learned from the
source dataset are biased when applied directly to the target classes. In this
paper, we study the transductive ZSH, i.e., we have unlabeled data for novel
classes. We put forward a simple yet efficient joint learning approach via
coarse-to-fine similarity mining which transfers knowledges from source data to
target data. It mainly consists of two building blocks in the proposed deep
architecture: 1) a shared two-streams network, which the first stream operates
on the source data and the second stream operates on the unlabeled data, to
learn the effective common image representations, and 2) a coarse-to-fine
module, which begins with finding the most representative images from target
classes and then further detect similarities among these images, to transfer
the similarities of the source data to the target data in a greedy fashion.
Extensive evaluation results on several benchmark datasets demonstrate that the
proposed hashing method achieves significant improvement over the
state-of-the-art methods.