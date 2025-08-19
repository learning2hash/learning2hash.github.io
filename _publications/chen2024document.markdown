---
layout: publication
title: 'Document Haystacks: Vision-language Reasoning Over Piles Of 1000+ Documents'
authors: Jun Chen, Dannong Xu, Junjie Fei, Chun-Mei Feng, Mohamed Elhoseiny
conference: Arxiv
year: 2024
bibkey: chen2024document
citations: 0
additional_links: [{name: Code, url: 'https://github.com/Vision-CAIR/dochaystacks'},
  {name: Paper, url: 'https://arxiv.org/abs/2411.16740'}]
tags: [Scalability, Datasets, Text Retrieval, Tools & Libraries, Evaluation]
short_authors: Chen et al.
---
Large multimodal models (LMMs) have achieved impressive progress in
vision-language understanding, yet they face limitations in real-world
applications requiring complex reasoning over a large number of images.
Existing benchmarks for multi-image question-answering are limited in scope,
each question is paired with only up to 30 images, which does not fully capture
the demands of large-scale retrieval tasks encountered in the real-world
usages. To reduce these gaps, we introduce two document haystack benchmarks,
dubbed DocHaystack and InfoHaystack, designed to evaluate LMM performance on
large-scale visual document retrieval and understanding. Additionally, we
propose V-RAG, a novel, vision-centric retrieval-augmented generation (RAG)
framework that leverages a suite of multimodal vision encoders, each optimized
for specific strengths, and a dedicated question-document relevance module.
V-RAG sets a new standard, with a 9% and 11% improvement in Recall@1 on the
challenging DocHaystack-1000 and InfoHaystack-1000 benchmarks, respectively,
compared to the previous best baseline models. Additionally, integrating V-RAG
with LMMs enables them to efficiently operate across thousands of images,
yielding significant improvements on our DocHaystack and InfoHaystack
benchmarks. Our code and datasets are available at
https://github.com/Vision-CAIR/dochaystacks