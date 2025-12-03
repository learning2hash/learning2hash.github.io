---
layout: publication
title: 'CLIP-PING: Boosting Lightweight Vision-language Models With Proximus Intrinsic
  Neighbors Guidance'
authors: Chu Myaet Thwal, Ye Lin Tun, Minh N. H. Nguyen, Eui-Nam Huh, Choong Seon
  Hong
conference: Arxiv
year: 2024
bibkey: thwal2024clip
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.03871'}]
tags: ["Evaluation", "Few Shot & Zero Shot", "Multimodal Retrieval", "Self-Supervised"]
short_authors: Thwal et al.
---
Beyond the success of Contrastive Language-Image Pre-training (CLIP), recent
trends mark a shift toward exploring the applicability of lightweight
vision-language models for resource-constrained scenarios. These models often
deliver suboptimal performance when relying solely on a single image-text
contrastive learning objective, spotlighting the need for more effective
training mechanisms that guarantee robust cross-modal feature alignment. In
this work, we propose CLIP-PING: Contrastive Language-Image Pre-training with
Proximus Intrinsic Neighbors Guidance, a novel yet simple and efficient
training paradigm designed to boost the performance of lightweight
vision-language models with minimal computational overhead and lower data
demands. CLIP-PING bootstraps unimodal features extracted from arbitrary
pre-trained encoders to obtain intrinsic guidance of proximus neighbor samples,
i.e., nearest-neighbor (NN) and cross nearest-neighbor (XNN). We find that
extra contrastive supervision from these neighbors substantially boosts
cross-modal alignment, enabling lightweight models to learn more generic
features with rich semantic diversity. Extensive experiments reveal that
CLIP-PING notably surpasses its peers in zero-shot generalization and
cross-modal retrieval tasks. Specifically, a 5.5% gain on zero-shot ImageNet1K
classification with 10.7% (I2T) and 5.7% (T2I) on Flickr30K retrieval, compared
to the original CLIP when using ViT-XS image encoder trained on 3 million
(image, text) pairs. Moreover, CLIP-PING showcases a strong transferability
under the linear evaluation protocol across several downstream tasks.