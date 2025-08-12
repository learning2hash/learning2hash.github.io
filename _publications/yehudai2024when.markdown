---
layout: publication
title: 'When Llms Are Unfit Use Fastfit: Fast And Effective Text Classification With
  Many Classes'
authors: Asaf Yehudai, Elron Bendel
conference: Arxiv
year: 2024
bibkey: yehudai2024when
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.12365'}]
tags: []
short_authors: Asaf Yehudai, Elron Bendel
---
We present FastFit, a method, and a Python package design to provide fast and
accurate few-shot classification, especially for scenarios with many
semantically similar classes. FastFit utilizes a novel approach integrating
batch contrastive learning and token-level similarity score. Compared to
existing few-shot learning packages, such as SetFit, Transformers, or few-shot
prompting of large language models via API calls, FastFit significantly
improves multiclass classification performance in speed and accuracy across
FewMany, our newly curated English benchmark, and Multilingual datasets.
FastFit demonstrates a 3-20x improvement in training speed, completing training
in just a few seconds. The FastFit package is now available on GitHub and PyPi,
presenting a user-friendly solution for NLP practitioners.