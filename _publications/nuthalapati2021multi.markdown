---
layout: publication
title: Multi-domain Few-shot Learning And Dataset For Agricultural Applications
authors: Sai Vidyaranya Nuthalapati, Anirudh Tunga
conference: 2021 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW)
year: 2021
bibkey: nuthalapati2021multi
citations: 37
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.09952'}]
tags: ["Datasets", "Few Shot & Zero Shot", "ICCV"]
short_authors: Sai Vidyaranya Nuthalapati, Anirudh Tunga
---
Automatic classification of pests and plants (both healthy and diseased) is
of paramount importance in agriculture to improve yield. Conventional deep
learning models based on convolutional neural networks require thousands of
labeled examples per category. In this work we propose a method to learn from a
few samples to automatically classify different pests, plants, and their
diseases, using Few-Shot Learning (FSL). We learn a feature extractor to
generate embeddings and then update the embeddings using Transformers. Using
Mahalanobis distance, a class-covariance-based metric, we then calculate the
similarity of the transformed embeddings with the embedding of the image to be
classified. Using our proposed architecture, we conduct extensive experiments
on multiple datasets showing the effectiveness of our proposed model. We
conduct 42 experiments in total to comprehensively analyze the model and it
achieves up to 14% and 24% performance gains on few-shot image classification
benchmarks on two datasets.
  We also compile a new FSL dataset containing images of healthy and diseased
plants taken in real-world settings. Using our proposed architecture which has
been shown to outperform several existing FSL architectures in agriculture, we
provide strong baselines on our newly proposed dataset.