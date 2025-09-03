---
layout: publication
title: Symmetric Multi-similarity Loss For EPIC-KITCHENS-100 Multi-instance Retrieval
  Challenge 2024
authors: Xiaoqi Wang, Yi Wang, Lap-Pui Chau
conference: Arxiv
year: 2024
bibkey: wang2024symmetric
citations: 0
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/2406.12256'}]
tags: ["Evaluation", "Text Retrieval"]
short_authors: Xiaoqi Wang, Yi Wang, Lap-Pui Chau
---
In this report, we present our champion solution for EPIC-KITCHENS-100
Multi-Instance Retrieval Challenge in CVPR 2024. Essentially, this challenge
differs from traditional visual-text retrieval tasks by providing a correlation
matrix that acts as a set of soft labels for video-text clip combinations.
However, existing loss functions have not fully exploited this information.
Motivated by this, we propose a novel loss function, Symmetric Multi-Similarity
Loss, which offers a more precise learning objective. Together with tricks and
ensemble learning, the model achieves 63.76% average mAP and 74.25% average
nDCG on the public leaderboard, demonstrating the effectiveness of our
approach. Our code will be released at:
https://github.com/xqwang14/SMS-Loss/tree/main