---
layout: publication
title: Retrieval Augmented Recipe Generation
authors: Guoshan Liu, Hailong Yin, Bin Zhu, Jingjing Chen, Chong-Wah Ngo, Yu-Gang
  Jiang
conference: Arxiv
year: 2024
bibkey: liu2024retrieval
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.08715'}]
tags: []
short_authors: Liu et al.
---
Given the potential applications of generating recipes from food images, this
area has garnered significant attention from researchers in recent years.
Existing works for recipe generation primarily utilize a two-stage training
method, first generating ingredients and then obtaining instructions from both
the image and ingredients. Large Multi-modal Models (LMMs), which have achieved
notable success across a variety of vision and language tasks, shed light to
generating both ingredients and instructions directly from images.
Nevertheless, LMMs still face the common issue of hallucinations during recipe
generation, leading to suboptimal performance. To tackle this, we propose a
retrieval augmented large multimodal model for recipe generation. We first
introduce Stochastic Diversified Retrieval Augmentation (SDRA) to retrieve
recipes semantically related to the image from an existing datastore as a
supplement, integrating them into the prompt to add diverse and rich context to
the input image. Additionally, Self-Consistency Ensemble Voting mechanism is
proposed to determine the most confident prediction recipes as the final
output. It calculates the consistency among generated recipe candidates, which
use different retrieval recipes as context for generation. Extensive
experiments validate the effectiveness of our proposed method, which
demonstrates state-of-the-art (SOTA) performance in recipe generation tasks on
the Recipe1M dataset.