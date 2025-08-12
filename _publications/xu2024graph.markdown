---
layout: publication
title: Graph Multi-similarity Learning For Molecular Property Prediction
authors: Hao Xu, Zhengyang Zhou, Pengyu Hong
conference: Arxiv
year: 2024
bibkey: xu2024graph
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.17615'}]
tags: ["Distance Metric Learning"]
short_authors: Hao Xu, Zhengyang Zhou, Pengyu Hong
---
Enhancing accurate molecular property prediction relies on effective and
proficient representation learning. It is crucial to incorporate diverse
molecular relationships characterized by multi-similarity (self-similarity and
relative similarities) between molecules. However, current molecular
representation learning methods fall short in exploring multi-similarity and
often underestimate the complexity of relationships between molecules.
Additionally, previous multi-similarity approaches require the specification of
positive and negative pairs to attribute distinct predefined weights to
different relative similarities, which can introduce potential bias. In this
work, we introduce Graph Multi-Similarity Learning for Molecular Property
Prediction (GraphMSL) framework, along with a novel approach to formulate a
generalized multi-similarity metric without the need to define positive and
negative pairs. In each of the chemical modality spaces (e.g.,molecular
depiction image, fingerprint, NMR, and SMILES) under consideration, we first
define a self-similarity metric (i.e., similarity between an anchor molecule
and another molecule), and then transform it into a generalized
multi-similarity metric for the anchor through a pair weighting function.
GraphMSL validates the efficacy of the multi-similarity metric across
MoleculeNet datasets. Furthermore, these metrics of all modalities are
integrated into a multimodal multi-similarity metric, which showcases the
potential to improve the performance. Moreover, the focus of the model can be
redirected or customized by altering the fusion function. Last but not least,
GraphMSL proves effective in drug discovery evaluations through post-hoc
analyses of the learnt representations.