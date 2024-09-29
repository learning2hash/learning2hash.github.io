---
layout: publication
title: Transductive Zero45;shot Hashing Via Coarse45;to45;fine Similarity Mining
authors: Lai Hanjiang, Pan Yan
conference: "Arxiv"
year: 2017
bibkey: lai2017transductive
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1711.02856"}
tags: ['ARXIV', 'Supervised']
---
Zero45;shot Hashing (ZSH) is to learn hashing models for novel/target classes without training data which is an important and challenging problem. Most existing ZSH approaches exploit transfer learning via an intermediate shared semantic representations between the seen/source classes and novel/target classes. However due to having disjoint the hash functions learned from the source dataset are biased when applied directly to the target classes. In this paper we study the transductive ZSH i.e. we have unlabeled data for novel classes. We put forward a simple yet efficient joint learning approach via coarse45;to45;fine similarity mining which transfers knowledges from source data to target data. It mainly consists of two building blocks in the proposed deep architecture 1) a shared two45;streams network which the first stream operates on the source data and the second stream operates on the unlabeled data to learn the effective common image representations and 2) a coarse45;to45;fine module which begins with finding the most representative images from target classes and then further detect similarities among these images to transfer the similarities of the source data to the target data in a greedy fashion. Extensive evaluation results on several benchmark datasets demonstrate that the proposed hashing method achieves significant improvement over the state45;of45;the45;art methods.
