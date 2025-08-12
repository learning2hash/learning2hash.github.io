---
layout: publication
title: Are Gender-neutral Queries Really Gender-neutral? Mitigating Gender Bias In
  Image Search
authors: Jialu Wang, Yang Liu, Xin Eric Wang
conference: Proceedings of the 2021 Conference on Empirical Methods in Natural Language
  Processing
year: 2021
bibkey: wang2021are
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.05433'}]
tags: ["EMNLP"]
short_authors: Jialu Wang, Yang Liu, Xin Eric Wang
---
Internet search affects people's cognition of the world, so mitigating biases
in search results and learning fair models is imperative for social good. We
study a unique gender bias in image search in this work: the search images are
often gender-imbalanced for gender-neutral natural language queries. We
diagnose two typical image search models, the specialized model trained on
in-domain datasets and the generalized representation model pre-trained on
massive image and text data across the internet. Both models suffer from severe
gender bias. Therefore, we introduce two novel debiasing approaches: an
in-processing fair sampling method to address the gender imbalance issue for
training models, and a post-processing feature clipping method base on mutual
information to debias multimodal representations of pre-trained models.
Extensive experiments on MS-COCO and Flickr30K benchmarks show that our methods
significantly reduce the gender bias in image search models.