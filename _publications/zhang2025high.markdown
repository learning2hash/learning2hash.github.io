---
layout: publication
title: High-order Nonlocal Hashing For Unsupervised Cross-modal Retrieval
authors: Zhang et al.
conference: World Wide Web
year: 2025
bibkey: zhang2025high
citations: 60
additional_links: [{name: Paper, url: 'https://link.springer.com/content/pdf/10.1007/s11280-020-00859-y.pdf'}]
tags: [Compact Codes, Multimodal Retrieval, Neural Hashing, Hashing Methods]
---
In light of the ability to enable efficient storage and fast query for big data, hashing techniques for cross-modal search have aroused extensive attention. Despite the great success achieved, unsupervised cross-modal hashing still suffers from lacking reliable similarity supervision and struggles with handling the heterogeneity issue between different modalities. To cope with these, in this paper, we devise a new deep hashing model, termed as High-order Nonlocal Hashing (HNH) to facilitate cross-modal retrieval with the following advantages. First, different from existing methods that mainly leverage low-level local-view similarity as the guidance for hashing learning, we propose a high-order affinity measure that considers the multi-modal neighbourhood structures from a nonlocal perspective, thereby comprehensively capturing the similarity relationships between data items. Second, a common representation is introduced to correlate different modalities. By enforcing the modal-specific descriptors and the common representation to be aligned with each other, the proposed HNH significantly bridges the modality gap and maintains the intra-consistency. Third, an effective affinity preserving objective function is delicately designed to generate high-quality binary codes. Extensive experiments evidence the superiority of the proposed HNH in unsupervised cross-modal retrieval tasks over the state-of-the-art baselines.