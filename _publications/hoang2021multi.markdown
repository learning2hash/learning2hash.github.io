---
layout: publication
title: 'Multi-modal Mutual Information Maximization: A Novel Approach For Unsupervised
  Deep Cross-modal Hashing'
authors: Hoang Tuan, Do Thanh-toan, Nguyen Tam V., Cheung Ngai-man
conference: Arxiv
year: 2021
bibkey: hoang2021multi
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.06489'}]
tags: ["Hashing-Methods", "Multimodal-Retrieval", "Datasets", "Evaluation", "Unsupervised"]
short_authors: Hoang et al.
---
In this paper, we adopt the maximizing mutual information (MI) approach to
tackle the problem of unsupervised learning of binary hash codes for efficient
cross-modal retrieval. We proposed a novel method, dubbed Cross-Modal Info-Max
Hashing (CMIMH). First, to learn informative representations that can preserve
both intra- and inter-modal similarities, we leverage the recent advances in
estimating variational lower-bound of MI to maximize the MI between the binary
representations and input features and between binary representations of
different modalities. By jointly maximizing these MIs under the assumption that
the binary representations are modelled by multivariate Bernoulli
distributions, we can learn binary representations, which can preserve both
intra- and inter-modal similarities, effectively in a mini-batch manner with
gradient descent. Furthermore, we find out that trying to minimize the modality
gap by learning similar binary representations for the same instance from
different modalities could result in less informative representations. Hence,
balancing between reducing the modality gap and losing modality-private
information is important for the cross-modal retrieval tasks. Quantitative
evaluations on standard benchmark datasets demonstrate that the proposed method
consistently outperforms other state-of-the-art cross-modal retrieval methods.