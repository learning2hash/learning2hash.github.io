---
layout: publication
title: Subspace Representation Learning For Few-shot Image Classification
authors: Ting-Yao Hu, Zhi-Qi Cheng, Alexander G. Hauptmann
conference: Arxiv
year: 2021
bibkey: hu2021subspace
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.00379'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Tools & Libraries"]
short_authors: Ting-Yao Hu, Zhi-Qi Cheng, Alexander G. Hauptmann
---
In this paper, we propose a subspace representation learning (SRL) framework
to tackle few-shot image classification tasks. It exploits a subspace in local
CNN feature space to represent an image, and measures the similarity between
two images according to a weighted subspace distance (WSD). When K images are
available for each class, we develop two types of template subspaces to
aggregate K-shot information: the prototypical subspace (PS) and the
discriminative subspace (DS). Based on the SRL framework, we extend metric
learning based techniques from vector to subspace representation. While most
previous works adopted global vector representation, using subspace
representation can effectively preserve the spatial structure, and diversity
within an image. We demonstrate the effectiveness of the SRL framework on three
public benchmark datasets: MiniImageNet, TieredImageNet and Caltech-UCSD
Birds-200-2011 (CUB), and the experimental results illustrate
competitive/superior performance of our method compared to the previous
state-of-the-art.