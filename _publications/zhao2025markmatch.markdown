---
layout: publication
title: 'Markmatch: Same-hand Stuffing Detection'
authors: Fei Zhao, Runlin Zhang, Chengcui Zhang, Nitesh Saxena
conference: 2025 IEEE International Conference on Multimedia and Expo Workshops (ICMEW)
year: 2025
bibkey: zhao2025markmatch
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.07032'}]
tags: ["Evaluation", "Self-Supervised", "Similarity Search"]
short_authors: Zhao et al.
---
We present MarkMatch, a retrieval system for detecting whether two paper ballot marks were filled by the same hand. Unlike the previous SOTA method BubbleSig, which used binary classification on isolated mark pairs, MarkMatch ranks stylistic similarity between a query mark and a mark in the database using contrastive learning. Our model is trained with a dense batch similarity matrix and a dual loss objective. Each sample is contrasted against many negatives within each batch, enabling the model to learn subtle handwriting difference and improve generalization under handwriting variation and visual noise, while diagonal supervision reinforces high confidence on true matches. The model achieves an F1 score of 0.943, surpassing BubbleSig's best performance. MarkMatch also integrates Segment Anything Model for flexible mark extraction via box- or point-based prompts. The system offers election auditors a practical tool for visual, non-biometric investigation of suspicious ballots.