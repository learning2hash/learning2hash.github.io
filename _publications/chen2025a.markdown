---
layout: publication
title: A 2D Semantic-aware Position Encoding For Vision Transformers
authors: Xi Chen, Shiyang Zhou, Muqi Huang, Jiaxu Feng, Yun Xiong, Kun Zhou, Biao
  Yang, Yuhui Zhang, Huishuai Bao, Sijia Peng, Chuan Li, Feng Shi
conference: Proceedings of the 27th ACM International Conference on Multimedia
year: 2025
bibkey: chen2025a
citations: 50
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.09466'}]
tags: ["Evaluation"]
short_authors: Chen et al.
---
Vision transformers have demonstrated significant advantages in computer vision tasks due to their ability to capture long-range dependencies and contextual relationships through self-attention. However, existing position encoding techniques, which are largely borrowed from natural language processing, fail to effectively capture semantic-aware positional relationships between image patches. Traditional approaches like absolute position encoding and relative position encoding primarily focus on 1D linear position relationship, often neglecting the semantic similarity between distant yet contextually related patches. These limitations hinder model generalization, translation equivariance, and the ability to effectively handle repetitive or structured patterns in images. In this paper, we propose 2-Dimensional Semantic-Aware Position Encoding (\(\text\{SaPE\}^2\)), a novel position encoding method with semantic awareness that dynamically adapts position representations by leveraging local content instead of fixed linear position relationship or spatial coordinates. Our method enhances the model's ability to generalize across varying image resolutions and scales, improves translation equivariance, and better aggregates features for visually similar but spatially distant patches. By integrating \(\text\{SaPE\}^2\) into vision transformers, we bridge the gap between position encoding and perceptual similarity, thereby improving performance on computer vision tasks.