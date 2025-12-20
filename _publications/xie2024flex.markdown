---
layout: publication
title: 'FLEX-CLIP: Feature-level Generation Network Enhanced CLIP For X-shot Cross-modal
  Retrieval'
authors: Jingyou Xie, Jiayi Kuang, Zhenzhou Lin, Jiarui Ouyang, Zishuo Zhao, Ying
  Shen
conference: Arxiv
year: 2024
bibkey: xie2024flex
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.17454'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Multimodal Retrieval"]
short_authors: Xie et al.
---
Given a query from one modality, few-shot cross-modal retrieval (CMR)
retrieves semantically similar instances in another modality with the target
domain including classes that are disjoint from the source domain. Compared
with classical few-shot CMR methods, vision-language pretraining methods like
CLIP have shown great few-shot or zero-shot learning performance. However, they
still suffer challenges due to (1) the feature degradation encountered in the
target domain and (2) the extreme data imbalance. To tackle these issues, we
propose FLEX-CLIP, a novel Feature-level Generation Network Enhanced CLIP.
FLEX-CLIP includes two training stages. In multimodal feature generation, we
propose a composite multimodal VAE-GAN network to capture real feature
distribution patterns and generate pseudo samples based on CLIP features,
addressing data imbalance. For common space projection, we develop a gate
residual network to fuse CLIP features with projected features, reducing
feature degradation in X-shot scenarios. Experimental results on four benchmark
datasets show a 7%-15% improvement over state-of-the-art methods, with ablation
studies demonstrating enhancement of CLIP features.