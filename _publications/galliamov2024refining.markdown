---
layout: publication
title: Refining Joint Text And Source Code Embeddings For Retrieval Task With Parameter-efficient
  Fine-tuning
authors: Karim Galliamov, Leila Khaertdinova, Karina Denisova
conference: Arxiv
year: 2024
bibkey: galliamov2024refining
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.04126'}]
tags: [Evaluation, Self-Supervised, Datasets, Tools & Libraries, Text Retrieval]
short_authors: Karim Galliamov, Leila Khaertdinova, Karina Denisova
---
The latest developments in Natural Language Processing (NLP) have
demonstrated remarkable progress in a code-text retrieval problem. As the
Transformer-based models used in this task continue to increase in size, the
computational costs and time required for end-to-end fine-tuning become
substantial. This poses a significant challenge for adapting and utilizing
these models when computational resources are limited. Motivated by these
concerns, we propose a fine-tuning framework that leverages Parameter-Efficient
Fine-Tuning (PEFT) techniques. Moreover, we adopt contrastive learning
objectives to improve the quality of bimodal representations learned by
transformer models. Additionally, for PEFT methods we provide extensive
benchmarking, the lack of which has been highlighted as a crucial problem in
the literature. Based on the thorough experimentation with the CodeT5+ model
conducted on two datasets, we demonstrate that the proposed fine-tuning
framework has the potential to improve code-text retrieval performance by
tuning only 0.4% parameters at most.