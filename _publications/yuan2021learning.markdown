---
layout: publication
title: Learning Class-level Prototypes For Few-shot Learning
authors: Minglei Yuan, Wenhai Wang, Tao Wang, Chunhao Cai, Qian Xu, Tong Lu
conference: Arxiv
year: 2021
bibkey: yuan2021learning
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.11072'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Yuan et al.
---
Few-shot learning aims to recognize new categories using very few labeled
samples. Although few-shot learning has witnessed promising development in
recent years, most existing methods adopt an average operation to calculate
prototypes, thus limited by the outlier samples. In this work, we propose a
simple yet effective framework for few-shot classification, which can learn to
generate preferable prototypes from few support data, with the help of an
episodic prototype generator module. The generated prototype is meant to be
close to a certain \textit\{\targetproto\{\}\} and is less influenced by outlier
samples. Extensive experiments demonstrate the effectiveness of this module,
and our approach gets a significant raise over baseline models, and get a
competitive result compared to previous methods on \textit\{mini\}ImageNet,
\textit\{tiered\}ImageNet, and cross-domain (\textit\{mini\}ImageNet \(\rightarrow\)
CUB-200-2011) datasets.