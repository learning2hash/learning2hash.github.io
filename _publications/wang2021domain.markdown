---
layout: publication
title: 'Domain-smoothing Network For Zero-shot Sketch-based Image Retrieval'
authors: Zhipeng Wang, Hao Wang, Jiexi Yan, Aming Wu, Cheng Deng
conference: "Arxiv"
year: 2021
citations: 25
bibkey: wang2021domain
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2106.11841'}
  - {name: "Code", url: 'https://github.com/haowang1992/DSN'}
tags: ['Cross-Modal', 'Retrieval Models', 'Shallow', 'Datasets', 'Has Code', 'Supervised', 'Applications']
---
Zero-Shot Sketch-Based Image Retrieval (ZS-SBIR) is a novel cross-modal
retrieval task, where abstract sketches are used as queries to retrieve natural
images under zero-shot scenario. Most existing methods regard ZS-SBIR as a
traditional classification problem and employ a cross-entropy or triplet-based
loss to achieve retrieval, which neglect the problems of the domain gap between
sketches and natural images and the large intra-class diversity in sketches.
Toward this end, we propose a novel Domain-Smoothing Network (DSN) for ZS-SBIR.
Specifically, a cross-modal contrastive method is proposed to learn generalized
representations to smooth the domain gap by mining relations with additional
augmented samples. Furthermore, a category-specific memory bank with sketch
features is explored to reduce intra-class diversity in the sketch domain.
Extensive experiments demonstrate that our approach notably outperforms the
state-of-the-art methods in both Sketchy and TU-Berlin datasets. Our source
code is publicly available at https://github.com/haowang1992/DSN.
