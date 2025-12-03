---
layout: publication
title: Face Recognition In The Age Of CLIP & Billion Image Datasets
authors: Aaditya Bhat, Shrey Jain
conference: Arxiv
year: 2023
bibkey: bhat2023face
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.07315'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Robustness"]
short_authors: Aaditya Bhat, Shrey Jain
---
CLIP (Contrastive Language-Image Pre-training) models developed by OpenAI
have achieved outstanding results on various image recognition and retrieval
tasks, displaying strong zero-shot performance. This means that they are able
to perform effectively on tasks for which they have not been explicitly
trained. Inspired by the success of OpenAI CLIP, a new publicly available
dataset called LAION-5B was collected which resulted in the development of open
ViT-H/14, ViT-G/14 models that outperform the OpenAI L/14 model. The LAION-5B
dataset also released an approximate nearest neighbor index, with a web
interface for search & subset creation.
  In this paper, we evaluate the performance of various CLIP models as
zero-shot face recognizers. Our findings show that CLIP models perform well on
face recognition tasks, but increasing the size of the CLIP model does not
necessarily lead to improved accuracy. Additionally, we investigate the
robustness of CLIP models against data poisoning attacks by testing their
performance on poisoned data. Through this analysis, we aim to understand the
potential consequences and misuse of search engines built using CLIP models,
which could potentially function as unintentional face recognition engines.