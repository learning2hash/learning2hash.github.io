---
layout: publication
title: Task-adaptive Asymmetric Deep Cross-modal Hashing
authors: Fengling Li, Tong Wang, Lei Zhu, Zheng Zhang, Xinhua Wang
conference: Arxiv
year: 2020
bibkey: li2020task
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.00197'}]
tags: ["Datasets", "Efficiency", "Hashing Methods", "Multimodal Retrieval", "Supervised"]
short_authors: Li et al.
---
Supervised cross-modal hashing aims to embed the semantic correlations of
heterogeneous modality data into the binary hash codes with discriminative
semantic labels. Because of its advantages on retrieval and storage efficiency,
it is widely used for solving efficient cross-modal retrieval. However,
existing researches equally handle the different tasks of cross-modal
retrieval, and simply learn the same couple of hash functions in a symmetric
way for them. Under such circumstance, the uniqueness of different cross-modal
retrieval tasks are ignored and sub-optimal performance may be brought.
Motivated by this, we present a Task-adaptive Asymmetric Deep Cross-modal
Hashing (TA-ADCMH) method in this paper. It can learn task-adaptive hash
functions for two sub-retrieval tasks via simultaneous modality representation
and asymmetric hash learning. Unlike previous cross-modal hashing approaches,
our learning framework jointly optimizes semantic preserving that transforms
deep features of multimedia data into binary hash codes, and the semantic
regression which directly regresses query modality representation to explicit
label. With our model, the binary codes can effectively preserve semantic
correlations across different modalities, meanwhile, adaptively capture the
query semantics. The superiority of TA-ADCMH is proved on two standard datasets
from many aspects.