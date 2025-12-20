---
layout: publication
title: 'Lacos-bloom: Low-rank Adaptation With Contrastive Objective On 8 Bits Siamese-bloom'
authors: Wen-Yu Hua, Brian Williams, Davood Shamsi
conference: Arxiv
year: 2023
bibkey: hua2023lacos
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.06404'}]
tags: ["Uncategorized"]
short_authors: Wen-Yu Hua, Brian Williams, Davood Shamsi
---
Text embeddings are useful features for several NLP applications, such as
sentence similarity, text clustering, and semantic search. In this paper, we
present a Low-rank Adaptation with a Contrastive objective on top of 8-bit
Siamese-BLOOM, a multilingual large language model optimized to produce
semantically meaningful word embeddings. The innovation is threefold. First, we
cast BLOOM weights to 8-bit values. Second, we fine-tune BLOOM with a scalable
adapter (LoRA) and 8-bit Adam optimizer for sentence similarity classification.
Third, we apply a Siamese architecture on BLOOM model with a contrastive
objective to ease the multi-lingual labeled data scarcity. The experiment
results show the quality of learned embeddings from LACoS-BLOOM is proportional
to the number of model parameters and the amount of unlabeled training data.
With the parameter efficient fine-tuning design, we are able to run BLOOM 7.1
billion parameters end-to-end on a single GPU machine with 32GB memory.
Compared to previous solution Sentence-BERT, we achieve significant improvement
on both English and multi-lingual STS tasks.