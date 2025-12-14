---
layout: publication
title: 'Procqa: A Large-scale Community-based Programming Question Answering Dataset
  For Code Search'
authors: Zehan Li, Jianfei Zhang, Chuantao Yin, Yuanxin Ouyang, Wenge Rong
conference: Arxiv
year: 2024
bibkey: li2024procqa
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.16702'}]
tags: [Scalability, Evaluation, Datasets]
short_authors: Li et al.
---
Retrieval-based code question answering seeks to match user queries in
natural language to relevant code snippets. Previous approaches typically rely
on pretraining models using crafted bi-modal and uni-modal datasets to align
text and code representations. In this paper, we introduce ProCQA, a
large-scale programming question answering dataset extracted from the
StackOverflow community, offering naturally structured mixed-modal QA pairs. To
validate its effectiveness, we propose a modality-agnostic contrastive
pre-training approach to improve the alignment of text and code representations
of current code language models. Compared to previous models that primarily
employ bimodal and unimodal pairs extracted from CodeSearchNet for
pre-training, our model exhibits significant performance improvements across a
wide range of code retrieval benchmarks.