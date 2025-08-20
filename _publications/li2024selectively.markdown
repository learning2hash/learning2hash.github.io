---
layout: publication
title: Selectively Hard Negative Mining For Alleviating Gradient Vanishing In Image-text
  Matching
authors: Zheng Li, Caili Guo, Xin Wang, Zerun Feng, Zhongtian Du
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2024
bibkey: li2024selectively
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.00181'}]
tags: [Distance Metric Learning, Evaluation]
short_authors: Li et al.
---
Recently, a series of Image-Text Matching (ITM) methods achieve impressive
performance. However, we observe that most existing ITM models suffer from
gradients vanishing at the beginning of training, which makes these models
prone to falling into local minima. Most ITM models adopt triplet loss with
Hard Negative mining (HN) as the optimization objective. We find that
optimizing an ITM model using only the hard negative samples can easily lead to
gradient vanishing. In this paper, we derive the condition under which the
gradient vanishes during training. When the difference between the positive
pair similarity and the negative pair similarity is close to 0, the gradients
on both the image and text encoders will approach 0. To alleviate the gradient
vanishing problem, we propose a Selectively Hard Negative Mining (SelHN)
strategy, which chooses whether to mine hard negative samples according to the
gradient vanishing condition. SelHN can be plug-and-play applied to existing
ITM models to give them better training behavior. To further ensure the
back-propagation of gradients, we construct a Residual Visual Semantic
Embedding model with SelHN, denoted as RVSE++. Extensive experiments on two ITM
benchmarks demonstrate the strength of RVSE++, achieving state-of-the-art
performance.