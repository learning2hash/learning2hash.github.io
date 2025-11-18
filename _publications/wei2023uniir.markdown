---
layout: publication
title: 'Uniir: Training And Benchmarking Universal Multimodal Information Retrievers'
authors: Cong Wei, Yang Chen, Haonan Chen, Hexiang Hu, Ge Zhang, Jie Fu, Alan Ritter,
  Wenhu Chen
conference: Lecture Notes in Computer Science
year: 2023
bibkey: wei2023uniir
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.17136'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot"]
short_authors: Wei et al.
---
Existing information retrieval (IR) models often assume a homogeneous format,
limiting their applicability to diverse user needs, such as searching for
images with text descriptions, searching for a news article with a headline
image, or finding a similar photo with a query image. To approach such
different information-seeking demands, we introduce UniIR, a unified
instruction-guided multimodal retriever capable of handling eight distinct
retrieval tasks across modalities. UniIR, a single retrieval system jointly
trained on ten diverse multimodal-IR datasets, interprets user instructions to
execute various retrieval tasks, demonstrating robust performance across
existing datasets and zero-shot generalization to new tasks. Our experiments
highlight that multi-task training and instruction tuning are keys to UniIR's
generalization ability. Additionally, we construct the M-BEIR, a multimodal
retrieval benchmark with comprehensive results, to standardize the evaluation
of universal multimodal information retrieval.