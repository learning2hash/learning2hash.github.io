---
layout: publication
title: Meta-mining Discriminative Samples For Kinship Verification
authors: Wanhua Li, Shiwei Wang, Jiwen Lu, Jianjiang Feng, Jie Zhou
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: li2021meta
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.15108'}]
tags: ["CVPR"]
short_authors: Li et al.
---
Kinship verification aims to find out whether there is a kin relation for a
given pair of facial images. Kinship verification databases are born with
unbalanced data. For a database with N positive kinship pairs, we naturally
obtain N(N-1) negative pairs. How to fully utilize the limited positive pairs
and mine discriminative information from sufficient negative samples for
kinship verification remains an open issue. To address this problem, we propose
a Discriminative Sample Meta-Mining (DSMM) approach in this paper. Unlike
existing methods that usually construct a balanced dataset with fixed negative
pairs, we propose to utilize all possible pairs and automatically learn
discriminative information from data. Specifically, we sample an unbalanced
train batch and a balanced meta-train batch for each iteration. Then we learn a
meta-miner with the meta-gradient on the balanced meta-train batch. In the end,
the samples in the unbalanced train batch are re-weighted by the learned
meta-miner to optimize the kinship models. Experimental results on the widely
used KinFaceW-I, KinFaceW-II, TSKinFace, and Cornell Kinship datasets
demonstrate the effectiveness of the proposed approach.