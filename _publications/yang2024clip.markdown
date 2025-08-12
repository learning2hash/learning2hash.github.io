---
layout: publication
title: 'CLIP-CID: Efficient CLIP Distillation Via Cluster-instance Discrimination'
authors: Kaicheng Yang, Tiancheng Gu, Xiang An, Haiqiang Jiang, Xiangzi Dai, Ziyong
  Feng, Weidong Cai, Jiankang Deng
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2025
bibkey: yang2024clip
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.09441'}]
tags: ["AAAI", "Efficiency", "Few Shot & Zero Shot"]
short_authors: Yang et al.
---
Contrastive Language-Image Pre-training (CLIP) has achieved excellent
performance over a wide range of tasks. However, the effectiveness of CLIP
heavily relies on a substantial corpus of pre-training data, resulting in
notable consumption of computational resources. Although knowledge distillation
has been widely applied in single modality models, how to efficiently expand
knowledge distillation to vision-language foundation models with extensive data
remains relatively unexplored. In this paper, we introduce CLIP-CID, a novel
distillation mechanism that effectively transfers knowledge from a large
vision-language foundation model to a smaller model. We initially propose a
simple but efficient image semantic balance method to reduce transfer learning
bias and improve distillation efficiency. This method filters out 43.7% of
image-text pairs from the LAION400M while maintaining superior performance.
After that, we leverage cluster-instance discrimination to facilitate knowledge
transfer from the teacher model to the student model, thereby empowering the
student model to acquire a holistic semantic comprehension of the pre-training
data. Experimental results demonstrate that CLIP-CID achieves state-of-the-art
performance on various downstream tasks including linear probe and zero-shot
classification.