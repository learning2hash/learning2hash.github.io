---
layout: publication
title: Webly Supervised Joint Embedding For Cross-modal Image-text Retrieval
authors: Niluthpol Chowdhury Mithun, Rameswar Panda, Evangelos E. Papalexakis, Amit
  K. Roy-Chowdhury
conference: Proceedings of the 26th ACM international conference on Multimedia
year: 2018
bibkey: mithun2018webly
citations: 78
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.07793'}]
tags: ["Datasets", "Image Retrieval", "Multimodal Retrieval", "Supervised"]
short_authors: Mithun et al.
---
Cross-modal retrieval between visual data and natural language description
remains a long-standing challenge in multimedia. While recent image-text
retrieval methods offer great promise by learning deep representations aligned
across modalities, most of these methods are plagued by the issue of training
with small-scale datasets covering a limited number of images with ground-truth
sentences. Moreover, it is extremely expensive to create a larger dataset by
annotating millions of images with sentences and may lead to a biased model.
Inspired by the recent success of webly supervised learning in deep neural
networks, we capitalize on readily-available web images with noisy annotations
to learn robust image-text joint representation. Specifically, our main idea is
to leverage web images and corresponding tags, along with fully annotated
datasets, in training for learning the visual-semantic joint embedding. We
propose a two-stage approach for the task that can augment a typical supervised
pair-wise ranking loss based formulation with weakly-annotated web images to
learn a more robust visual-semantic embedding. Experiments on two standard
benchmark datasets demonstrate that our method achieves a significant
performance gain in image-text retrieval compared to state-of-the-art
approaches.