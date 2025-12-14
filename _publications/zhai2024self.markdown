---
layout: publication
title: Self-adaptive Multimodal Retrieval-augmented Generation
authors: Wenjia Zhai
conference: Arxiv
year: 2024
bibkey: zhai2024self
citations: 2
additional_links: [{name: Code, url: 'https://github.com/SAM-RAG/SAM_RAG'}, {name: Paper,
    url: 'https://arxiv.org/abs/2410.11321'}]
tags: [Evaluation, Multimodal Retrieval]
short_authors: Wenjia Zhai
---
Traditional Retrieval-Augmented Generation (RAG) methods are limited by their
reliance on a fixed number of retrieved documents, often resulting in
incomplete or noisy information that undermines task performance. Although
recent adaptive approaches alleviated these problems, their application in
intricate and real-world multimodal tasks remains limited. To address these, we
propose a new approach called Self-adaptive Multimodal Retrieval-Augmented
Generation (SAM-RAG), tailored specifically for multimodal contexts. SAM-RAG
not only dynamically filters relevant documents based on the input query,
including image captions when needed, but also verifies the quality of both the
retrieved documents and the output. Extensive experimental results show that
SAM-RAG surpasses existing state-of-the-art methods in both retrieval accuracy
and response generation. By further ablation experiments and effectiveness
analysis, SAM-RAG maintains high recall quality while improving overall task
performance in multimodal RAG task. Our codes are available at
https://github.com/SAM-RAG/SAM_RAG.