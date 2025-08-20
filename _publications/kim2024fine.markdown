---
layout: publication
title: Fine-tuning CLIP Text Encoders With Two-step Paraphrasing
authors: Hyunjae Kim, Seunghyun Yoon, Trung Bui, Handong Zhao, Quan Tran, Franck Dernoncourt,
  Jaewoo Kang
conference: Arxiv
year: 2024
bibkey: kim2024fine
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.15120'}]
tags: [Multimodal Retrieval, Large-Scale Search, Image Retrieval, Scalability]
short_authors: Kim et al.
---
Contrastive language-image pre-training (CLIP) models have demonstrated
considerable success across various vision-language tasks, such as
text-to-image retrieval, where the model is required to effectively process
natural language input to produce an accurate visual output. However, current
models still face limitations in dealing with linguistic variations in input
queries, such as paraphrases, making it challenging to handle a broad range of
user queries in real-world applications. In this study, we introduce a
straightforward fine-tuning approach to enhance the representations of CLIP
models for paraphrases. Our approach involves a two-step paraphrase generation
process, where we automatically create two categories of paraphrases from
web-scale image captions by leveraging large language models. Subsequently, we
fine-tune the CLIP text encoder using these generated paraphrases while
freezing the image encoder. Our resulting model, which we call ParaCLIP,
exhibits significant improvements over baseline CLIP models across various
tasks, including paraphrased retrieval (with rank similarity scores improved by
up to 2.0% and 5.6%), Visual Genome Relation and Attribution, as well as seven
semantic textual similarity tasks.