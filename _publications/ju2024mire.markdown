---
layout: publication
title: 'Mire: Enhancing Multimodal Queries Representation Via Fusion-free Modality
  Interaction For Multimodal Retrieval'
authors: Yeong-Joon Ju, Ho-Joong Kim, Seong-Whan Lee
conference: Arxiv
year: 2024
bibkey: ju2024mire
citations: 0
additional_links: [{name: Code, url: 'https://github.com/yeongjoonJu/MIRe'}, {name: Paper,
    url: 'https://arxiv.org/abs/2411.08334'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Multimodal Retrieval", "Tools & Libraries"]
short_authors: Yeong-Joon Ju, Ho-Joong Kim, Seong-Whan Lee
---
Recent multimodal retrieval methods have endowed text-based retrievers with multimodal capabilities by utilizing pre-training strategies for visual-text alignment. They often directly fuse the two modalities for cross-reference during the alignment to understand multimodal queries. However, existing methods often overlook crucial visual information due to a text-dominant issue, which overly depends on text-driven signals. In this paper, we introduce MIRe, a retrieval framework that achieves modality interaction without fusing textual features during the alignment. Our method allows the textual query to attend to visual embeddings while not feeding text-driven signals back into the visual representations. Additionally, we construct a pre-training dataset for multimodal query retrieval by transforming concise question-answer pairs into extended passages. Our experiments demonstrate that our pre-training strategy significantly enhances the understanding of multimodal queries, resulting in strong performance across four multimodal retrieval benchmarks under zero-shot settings. Moreover, our ablation studies and analyses explicitly verify the effectiveness of our framework in mitigating the text-dominant issue. Our code is publicly available: https://github.com/yeongjoonJu/MIRe