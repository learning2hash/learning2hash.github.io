---
layout: publication
title: 'Catlip: Clip-level Visual Recognition Accuracy With 2.7x Faster Pre-training
  On Web-scale Image-text Data'
authors: Sachin Mehta, Maxwell Horton, Fartash Faghri, Mohammad Hossein Sekhavat,
  Mahyar Najibi, Mehrdad Farajtabar, Oncel Tuzel, Mohammad Rastegari
conference: Arxiv
year: 2024
bibkey: mehta2024catlip
citations: 0
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/2404.15653'}]
tags: ["Distance Metric Learning", "Large Scale Search", "Scalability", "Self-Supervised", "Supervised"]
short_authors: Mehta et al.
---
Contrastive learning has emerged as a transformative method for learning
effective visual representations through the alignment of image and text
embeddings. However, pairwise similarity computation in contrastive loss
between image and text pairs poses computational challenges. This paper
presents a novel weakly supervised pre-training of vision models on web-scale
image-text data. The proposed method reframes pre-training on image-text data
as a classification task. Consequently, it eliminates the need for pairwise
similarity computations in contrastive loss, achieving a remarkable \(2.7\times\)
acceleration in training speed compared to contrastive learning on web-scale
data. Through extensive experiments spanning diverse vision tasks, including
detection and segmentation, we demonstrate that the proposed method maintains
high representation quality. Our source code along with pre-trained model
weights and training recipes is available at
https://github.com/apple/corenet.