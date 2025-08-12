---
layout: publication
title: 'Colorflow: Retrieval-augmented Image Sequence Colorization'
authors: Junhao Zhuang, Xuan Ju, Zhaoyang Zhang, Yong Liu, Shiyi Zhang, Chun Yuan,
  Ying Shan
conference: Arxiv
year: 2024
bibkey: zhuang2024colorflow
citations: 0
additional_links: [{name: Code, url: 'https://zhuang2002.github.io/ColorFlow/'}, {
    name: Paper, url: 'https://arxiv.org/abs/2412.11815'}]
tags: []
short_authors: Zhuang et al.
---
Automatic black-and-white image sequence colorization while preserving
character and object identity (ID) is a complex task with significant market
demand, such as in cartoon or comic series colorization. Despite advancements
in visual colorization using large-scale generative models like diffusion
models, challenges with controllability and identity consistency persist,
making current solutions unsuitable for industrial application.To address this,
we propose ColorFlow, a three-stage diffusion-based framework tailored for
image sequence colorization in industrial applications. Unlike existing methods
that require per-ID finetuning or explicit ID embedding extraction, we propose
a novel robust and generalizable Retrieval Augmented Colorization pipeline for
colorizing images with relevant color references. Our pipeline also features a
dual-branch design: one branch for color identity extraction and the other for
colorization, leveraging the strengths of diffusion models. We utilize the
self-attention mechanism in diffusion models for strong in-context learning and
color identity matching. To evaluate our model, we introduce ColorFlow-Bench, a
comprehensive benchmark for reference-based colorization. Results show that
ColorFlow outperforms existing models across multiple metrics, setting a new
standard in sequential image colorization and potentially benefiting the art
industry. We release our codes and models on our project page:
https://zhuang2002.github.io/ColorFlow/.