---
layout: publication
title: Part-guided Attention Learning For Vehicle Instance Retrieval
authors: Xinyu Zhang, Rufeng Zhang, Jiewei Cao, Dong Gong, Mingyu You, Chunhua Shen
conference: IEEE Transactions on Intelligent Transportation Systems
year: 2020
bibkey: zhang2019part
citations: 56
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.06023'}]
tags: ["Datasets", "Evaluation", "Scalability"]
short_authors: Zhang et al.
---
Vehicle instance retrieval often requires one to recognize the fine-grained
visual differences between vehicles. Besides the holistic appearance of
vehicles which is easily affected by the viewpoint variation and distortion,
vehicle parts also provide crucial cues to differentiate near-identical
vehicles. Motivated by these observations, we introduce a Part-Guided Attention
Network (PGAN) to pinpoint the prominent part regions and effectively combine
the global and part information for discriminative feature learning. PGAN first
detects the locations of different part components and salient regions
regardless of the vehicle identity, which serve as the bottom-up attention to
narrow down the possible searching regions. To estimate the importance of
detected parts, we propose a Part Attention Module (PAM) to adaptively locate
the most discriminative regions with high-attention weights and suppress the
distraction of irrelevant parts with relatively low weights. The PAM is guided
by the instance retrieval loss and therefore provides top-down attention that
enables attention to be calculated at the level of car parts and other salient
regions. Finally, we aggregate the global appearance and part features to
improve the feature performance further. The PGAN combines part-guided
bottom-up and top-down attention, global and part visual features in an
end-to-end framework. Extensive experiments demonstrate that the proposed
method achieves new state-of-the-art vehicle instance retrieval performance on
four large-scale benchmark datasets.