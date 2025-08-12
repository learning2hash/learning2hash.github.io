---
layout: publication
title: 'Msdnet: Multi-scale Decoder For Few-shot Semantic Segmentation Via Transformer-guided
  Prototyping'
authors: Amirreza Fateh, Mohammad Reza Mohammadi, Mohammad Reza Jahed Motlagh
conference: Arxiv
year: 2024
bibkey: fateh2024msdnet
citations: 3
additional_links: [{name: Code, url: 'https://github.com/amirrezafateh/MSDNet'}, {
    name: Paper, url: 'https://arxiv.org/abs/2409.11316'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Amirreza Fateh, Mohammad Reza Mohammadi, Mohammad Reza Jahed Motlagh
---
Few-shot Semantic Segmentation addresses the challenge of segmenting objects in query images with only a handful of annotated examples. However, many previous state-of-the-art methods either have to discard intricate local semantic features or suffer from high computational complexity. To address these challenges, we propose a new Few-shot Semantic Segmentation framework based on the Transformer architecture. Our approach introduces the spatial transformer decoder and the contextual mask generation module to improve the relational understanding between support and query images. Moreover, we introduce a multi scale decoder to refine the segmentation mask by incorporating features from different resolutions in a hierarchical manner. Additionally, our approach integrates global features from intermediate encoder stages to improve contextual understanding, while maintaining a lightweight structure to reduce complexity. This balance between performance and efficiency enables our method to achieve competitive results on benchmark datasets such as PASCAL-5^i and COCO-20^i in both 1-shot and 5-shot settings. Notably, our model with only 1.5 million parameters demonstrates competitive performance while overcoming limitations of existing methodologies. https://github.com/amirrezafateh/MSDNet