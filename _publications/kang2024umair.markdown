---
layout: publication
title: 'UMAIR-FPS: User-aware Multi-modal Animation Illustration Recommendation Fusion
  With Painting Style'
authors: Yan Kang, Hao Lin, Mingjian Yang, Shin-jye Lee
conference: Lecture Notes in Computer Science
year: 2025
bibkey: kang2024umair
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.10381'}]
tags: ["Recommender Systems"]
short_authors: Kang et al.
---
The rapid advancement of high-quality image generation models based on AI has
generated a deluge of anime illustrations. Recommending illustrations to users
within massive data has become a challenging and popular task. However,
existing anime recommendation systems have focused on text features but still
need to integrate image features. In addition, most multi-modal recommendation
research is constrained by tightly coupled datasets, limiting its applicability
to anime illustrations. We propose the User-aware Multi-modal Animation
Illustration Recommendation Fusion with Painting Style (UMAIR-FPS) to tackle
these gaps. In the feature extract phase, for image features, we are the first
to combine image painting style features with semantic features to construct a
dual-output image encoder for enhancing representation. For text features, we
obtain text embeddings based on fine-tuning Sentence-Transformers by
incorporating domain knowledge that composes a variety of domain text pairs
from multilingual mappings, entity relationships, and term explanation
perspectives, respectively. In the multi-modal fusion phase, we novelly propose
a user-aware multi-modal contribution measurement mechanism to weight
multi-modal features dynamically according to user features at the interaction
level and employ the DCN-V2 module to model bounded-degree multi-modal crosses
effectively. UMAIR-FPS surpasses the stat-of-the-art baselines on large
real-world datasets, demonstrating substantial performance enhancements.