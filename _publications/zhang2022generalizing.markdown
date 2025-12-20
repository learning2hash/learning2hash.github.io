---
layout: publication
title: Generalizing Multimodal Pre-training Into Multilingual Via Language Acquisition
authors: Liang Zhang, Anwen Hu, Qin Jin
conference: Arxiv
year: 2022
bibkey: zhang2022generalizing
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.11091'}]
tags: ["Evaluation", "Text Retrieval", "Tools & Libraries"]
short_authors: Liang Zhang, Anwen Hu, Qin Jin
---
English-based Vision-Language Pre-training (VLP) has achieved great success
in various downstream tasks. Some efforts have been taken to generalize this
success to non-English languages through Multilingual Vision-Language
Pre-training (M-VLP). However, due to the large number of languages, M-VLP
models often require huge computing resources and cannot be flexibly extended
to new languages. In this work, we propose a \textbf\{M\}ulti\textbf\{L\}ingual
\textbf\{A\}cquisition (MLA) framework that can easily generalize a monolingual
Vision-Language Pre-training model into multilingual. Specifically, we design a
lightweight language acquisition encoder based on state-of-the-art monolingual
VLP models. We further propose a two-stage training strategy to optimize the
language acquisition encoder, namely the Native Language Transfer stage and the
Language Exposure stage. With much less multilingual training data and
computing resources, our model achieves state-of-the-art performance on
multilingual image-text and video-text retrieval benchmarks.