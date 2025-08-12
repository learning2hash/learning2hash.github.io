---
layout: publication
title: A Simple And Effective Method To Improve Zero-shot Cross-lingual Transfer Learning
authors: Kunbo Ding, Weijie Liu, Yuejian Fang, Weiquan Mao, Zhe Zhao, Tao Zhu, Haoyan
  Liu, Rong Tian, Yiren Chen
conference: Arxiv
year: 2022
bibkey: ding2022simple
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.09934'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Ding et al.
---
Existing zero-shot cross-lingual transfer methods rely on parallel corpora or
bilingual dictionaries, which are expensive and impractical for low-resource
languages. To disengage from these dependencies, researchers have explored
training multilingual models on English-only resources and transferring them to
low-resource languages. However, its effect is limited by the gap between
embedding clusters of different languages. To address this issue, we propose
Embedding-Push, Attention-Pull, and Robust targets to transfer English
embeddings to virtual multilingual embeddings without semantic loss, thereby
improving cross-lingual transferability. Experimental results on mBERT and
XLM-R demonstrate that our method significantly outperforms previous works on
the zero-shot cross-lingual text classification task and can obtain a better
multilingual alignment.