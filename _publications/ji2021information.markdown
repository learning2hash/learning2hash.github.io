---
layout: publication
title: 'Information Symmetry Matters: A Modal-alternating Propagation Network For
  Few-shot Learning'
authors: Zhong Ji, Zhishen Hou, Xiyao Liu, Yanwei Pang, Jungong Han
conference: IEEE Transactions on Image Processing
year: 2022
bibkey: ji2021information
citations: 31
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.01295'}]
tags: []
short_authors: Ji et al.
---
Semantic information provides intra-class consistency and inter-class
discriminability beyond visual concepts, which has been employed in Few-Shot
Learning (FSL) to achieve further gains. However, semantic information is only
available for labeled samples but absent for unlabeled samples, in which the
embeddings are rectified unilaterally by guiding the few labeled samples with
semantics. Therefore, it is inevitable to bring a cross-modal bias between
semantic-guided samples and nonsemantic-guided samples, which results in an
information asymmetry problem. To address this problem, we propose a
Modal-Alternating Propagation Network (MAP-Net) to supplement the absent
semantic information of unlabeled samples, which builds information symmetry
among all samples in both visual and semantic modalities. Specifically, the
MAP-Net transfers the neighbor information by the graph propagation to generate
the pseudo-semantics for unlabeled samples guided by the completed visual
relationships and rectify the feature embeddings. In addition, due to the large
discrepancy between visual and semantic modalities, we design a Relation
Guidance (RG) strategy to guide the visual relation vectors via semantics so
that the propagated information is more beneficial. Extensive experimental
results on three semantic-labeled datasets, i.e., Caltech-UCSD-Birds 200-2011,
SUN Attribute Database, and Oxford 102 Flower, have demonstrated that our
proposed method achieves promising performance and outperforms the
state-of-the-art approaches, which indicates the necessity of information
symmetry.