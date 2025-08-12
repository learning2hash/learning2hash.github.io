---
layout: publication
title: Exploring Multi-view Pixel Contrast For General And Robust Image Forgery Localization
authors: Zijie Lou, Gang Cao, Kun Guo, Haochen Zhu, Lifang Yu
conference: IEEE Transactions on Information Forensics and Security
year: 2025
bibkey: lou2024exploring
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.13565'}]
tags: ["Robustness"]
short_authors: Lou et al.
---
Image forgery localization, which aims to segment tampered regions in an
image, is a fundamental yet challenging digital forensic task. While some deep
learning-based forensic methods have achieved impressive results, they directly
learn pixel-to-label mappings without fully exploiting the relationship between
pixels in the feature space. To address such deficiency, we propose a
Multi-view Pixel-wise Contrastive algorithm (MPC) for image forgery
localization. Specifically, we first pre-train the backbone network with the
supervised contrastive loss to model pixel relationships from the perspectives
of within-image, cross-scale and cross-modality. That is aimed at increasing
intra-class compactness and inter-class separability. Then the localization
head is fine-tuned using the cross-entropy loss, resulting in a better pixel
localizer. The MPC is trained on three different scale training datasets to
make a comprehensive and fair comparison with existing image forgery
localization algorithms. Extensive experiments on the small, medium and large
scale training datasets show that the proposed MPC achieves higher
generalization performance and robustness against post-processing than the
state-of-the-arts. Code will be available at
https://github.com/multimediaFor/MPC.