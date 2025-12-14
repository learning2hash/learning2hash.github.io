---
layout: publication
title: Scaling Prompt Instructed Zero Shot Composed Image Retrieval With Image-only
  Data
authors: Yiqun Duan, Sameera Ramasinghe, Stephen Gould, Ajanthan Thalaiyasingam
conference: 2025 International Joint Conference on Neural Networks (IJCNN)
year: 2025
bibkey: duan2025scaling
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.00812'}]
tags: [Evaluation, Supervised, Image Retrieval, Few-shot & Zero-shot, Datasets, Scalability]
short_authors: Duan et al.
---
Composed Image Retrieval (CIR) is the task of retrieving images matching a reference image augmented with a text, where the text describes changes to the reference image in natural language. Traditionally, models designed for CIR have relied on triplet data containing a reference image, reformulation text, and a target image. However, curating such triplet data often necessitates human intervention, leading to prohibitive costs. This challenge has hindered the scalability of CIR model training even with the availability of abundant unlabeled data. With the recent advances in foundational models, we advocate a shift in the CIR training paradigm where human annotations can be efficiently replaced by large language models (LLMs). Specifically, we demonstrate the capability of large captioning and language models in efficiently generating data for CIR only relying on unannotated image collections. Additionally, we introduce an embedding reformulation architecture that effectively combines image and text modalities. Our model, named InstructCIR, outperforms state-of-the-art methods in zero-shot composed image retrieval on CIRR and FashionIQ datasets. Furthermore, we demonstrate that by increasing the amount of generated data, our zero-shot model gets closer to the performance of supervised baselines.