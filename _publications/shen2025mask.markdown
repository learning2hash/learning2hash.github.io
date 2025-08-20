---
layout: publication
title: 'Mask-aware Text-to-image Retrieval: Referring Expression Segmentation Meets
  Cross-modal Retrieval'
authors: Li-Cheng Shen, Jih-Kang Hsieh, Wei-Hua Li, Chu-Song Chen
conference: Proceedings of the 2025 International Conference on Multimedia Retrieval
year: 2025
bibkey: shen2025mask
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.22864'}]
tags: [Multimodal Retrieval, Tools & Libraries, Datasets, Image Retrieval]
short_authors: Shen et al.
---
Text-to-image retrieval (TIR) aims to find relevant images based on a textual query, but existing approaches are primarily based on whole-image captions and lack interpretability. Meanwhile, referring expression segmentation (RES) enables precise object localization based on natural language descriptions but is computationally expensive when applied across large image collections. To bridge this gap, we introduce Mask-aware TIR (MaTIR), a new task that unifies TIR and RES, requiring both efficient image search and accurate object segmentation. To address this task, we propose a two-stage framework, comprising a first stage for segmentation-aware image retrieval and a second stage for reranking and object grounding with a multimodal large language model (MLLM). We leverage SAM 2 to generate object masks and Alpha-CLIP to extract region-level embeddings offline at first, enabling effective and scalable online retrieval. Secondly, MLLM is used to refine retrieval rankings and generate bounding boxes, which are matched to segmentation masks. We evaluate our approach on COCO and D\(^3\) datasets, demonstrating significant improvements in both retrieval accuracy and segmentation quality over previous methods.