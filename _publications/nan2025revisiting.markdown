---
layout: publication
title: Revisiting Medical Image Retrieval Via Knowledge Consolidation
authors: Yang Nan, Huichi Zhou, Xiaodan Xing, Giorgos Papanastasiou, Lei Zhu, Zhifan
  Gao, Alejandro F Fangi, Guang Yang
conference: Medical Image Analysis
year: 2025
bibkey: nan2025revisiting
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.09370'}]
tags: [Evaluation, Image Retrieval, Datasets, Robustness, Tools & Libraries, Hashing
    Methods, Recommender Systems]
short_authors: Nan et al.
---
As artificial intelligence and digital medicine increasingly permeate healthcare systems, robust governance frameworks are essential to ensure ethical, secure, and effective implementation. In this context, medical image retrieval becomes a critical component of clinical data management, playing a vital role in decision-making and safeguarding patient information. Existing methods usually learn hash functions using bottleneck features, which fail to produce representative hash codes from blended embeddings. Although contrastive hashing has shown superior performance, current approaches often treat image retrieval as a classification task, using category labels to create positive/negative pairs. Moreover, many methods fail to address the out-of-distribution (OOD) issue when models encounter external OOD queries or adversarial attacks. In this work, we propose a novel method to consolidate knowledge of hierarchical features and optimisation functions. We formulate the knowledge consolidation by introducing Depth-aware Representation Fusion (DaRF) and Structure-aware Contrastive Hashing (SCH). DaRF adaptively integrates shallow and deep representations into blended features, and SCH incorporates image fingerprints to enhance the adaptability of positive/negative pairings. These blended features further facilitate OOD detection and content-based recommendation, contributing to a secure AI-driven healthcare environment. Moreover, we present a content-guided ranking to improve the robustness and reproducibility of retrieval results. Our comprehensive assessments demonstrate that the proposed method could effectively recognise OOD samples and significantly outperform existing approaches in medical image retrieval (p<0.05). In particular, our method achieves a 5.6-38.9% improvement in mean Average Precision on the anatomical radiology dataset.