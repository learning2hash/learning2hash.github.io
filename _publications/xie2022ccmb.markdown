---
layout: publication
title: 'CCMB: A Large-scale Chinese Cross-modal Benchmark'
authors: Chunyu Xie, Heng Cai, Jincheng Li, Fanjing Kong, Xiaoyu Wu, Jianfei Song,
  Henrique Morimitsu, Lin Yao, Dexin Wang, Xiangzheng Zhang, Dawei Leng, Baochang
  Zhang, Xiangyang Ji, Yafeng Deng
conference: Proceedings of the 31st ACM International Conference on Multimedia (ACM
  MM) 2023 Pages 4219-4227
year: 2022
bibkey: xie2022ccmb
citations: 1
additional_links: [{name: Code, url: 'https://github.com/yuxie11/R2D2'}, {name: Paper,
    url: 'https://arxiv.org/abs/2205.03860'}]
tags: [Evaluation, Re-ranking, Few-shot & Zero-shot, Datasets, Scalability, Tools
    & Libraries, Text Retrieval, Hybrid ANN Methods]
short_authors: Xie et al.
---
Vision-language pre-training (VLP) on large-scale datasets has shown premier
performance on various downstream tasks. In contrast to plenty of available
benchmarks with English corpus, large-scale pre-training datasets and
downstream datasets with Chinese corpus remain largely unexplored. In this
work, we build a large-scale high-quality Chinese Cross-Modal Benchmark named
CCMB for the research community, which contains the currently largest public
pre-training dataset Zero and five human-annotated fine-tuning datasets for
downstream tasks. Zero contains 250 million images paired with 750 million text
descriptions, plus two of the five fine-tuning datasets are also currently the
largest ones for Chinese cross-modal downstream tasks. Along with the CCMB, we
also develop a VLP framework named R2D2, applying a pre-Ranking + Ranking
strategy to learn powerful vision-language representations and a two-way
distillation method (i.e., target-guided Distillation and feature-guided
Distillation) to further enhance the learning capability. With the Zero and the
R2D2 VLP framework, we achieve state-of-the-art performance on twelve
downstream datasets from five broad categories of tasks including image-text
retrieval, image-text matching, image caption, text-to-image generation, and
zero-shot image classification. The datasets, models, and codes are available
at https://github.com/yuxie11/R2D2