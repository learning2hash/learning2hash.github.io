---
layout: publication
title: 'NLIP: Noise-robust Language-image Pre-training'
authors: Runhui Huang, Yanxin Long, Jianhua Han, Hang Xu, Xiwen Liang, Chunjing Xu,
  Xiaodan Liang
conference: Arxiv
year: 2022
bibkey: huang2022nlip
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.07086'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Text Retrieval", "Tools & Libraries"]
short_authors: Huang et al.
---
Large-scale cross-modal pre-training paradigms have recently shown ubiquitous
success on a wide range of downstream tasks, e.g., zero-shot classification,
retrieval and image captioning. However, their successes highly rely on the
scale and quality of web-crawled data that naturally contain incomplete and
noisy information (e.g., wrong or irrelevant content). Existing works either
design manual rules to clean data or generate pseudo-targets as auxiliary
signals for reducing noise impact, which do not explicitly tackle both the
incorrect and incomplete challenges simultaneously. In this paper, to
automatically mitigate the impact of noise by solely mining over existing data,
we propose a principled Noise-robust Language-Image Pre-training framework
(NLIP) to stabilize pre-training via two schemes: noise-harmonization and
noise-completion. First, in noise-harmonization scheme, NLIP estimates the
noise probability of each pair according to the memorization effect of
cross-modal transformers, then adopts noise-adaptive regularization to
harmonize the cross-modal alignments with varying degrees. Second, in
noise-completion scheme, to enrich the missing object information of text, NLIP
injects a concept-conditioned cross-modal decoder to obtain semantic-consistent
synthetic captions to complete noisy ones, which uses the retrieved visual
concepts (i.e., objects' names) for the corresponding image to guide captioning
generation. By collaboratively optimizing noise-harmonization and
noise-completion schemes, our NLIP can alleviate the common noise effects
during image-text pre-training in a more efficient way. Extensive experiments
show the significant performance improvements of our NLIP using only 26M data
over existing pre-trained models (e.g., CLIP, FILIP and BLIP) on 12 zero-shot
classification datasets, MSCOCO image captioning and zero-shot image-text
retrieval tasks.