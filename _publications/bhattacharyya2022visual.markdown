---
layout: publication
title: 'Visual Representation Learning With Self-supervised Attention For Low-label High-data Regime'
authors: Prarthana Bhattacharyya, Chenge Li, Xiaonan Zhao, István Fehérvári, Jason Sun
conference: "Arxiv"
year: 2022
citations: 1
bibkey: bhattacharyya2022visual
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2201.08951'}
  - {name: "Code", url: 'https://github.com/AutoVision-cloud/SSL-ViT-lowlabel-highdata'}
tags: ['Cross-Modal', 'Deep', 'Model Design', 'Retrieval Models', 'Datasets', 'Vector Indexing', 'Has Code', 'Supervised', 'Similarity Learning', 'Applications']
---
Self-supervision has shown outstanding results for natural language
processing, and more recently, for image recognition. Simultaneously, vision
transformers and its variants have emerged as a promising and scalable
alternative to convolutions on various computer vision tasks. In this paper, we
are the first to question if self-supervised vision transformers (SSL-ViTs) can
be adapted to two important computer vision tasks in the low-label, high-data
regime: few-shot image classification and zero-shot image retrieval. The
motivation is to reduce the number of manual annotations required to train a
visual embedder, and to produce generalizable and semantically meaningful
embeddings. For few-shot image classification we train SSL-ViTs without any
supervision, on external data, and use this trained embedder to adapt quickly
to novel classes with limited number of labels. For zero-shot image retrieval,
we use SSL-ViTs pre-trained on a large dataset without any labels and fine-tune
them with several metric learning objectives. Our self-supervised attention
representations outperforms the state-of-the-art on several public benchmarks
for both tasks, namely miniImageNet and CUB200 for few-shot image
classification by up-to 6%-10%, and Stanford Online Products, Cars196 and
CUB200 for zero-shot image retrieval by up-to 4%-11%. Code is available at
\url\{https://github.com/AutoVision-cloud/SSL-ViT-lowlabel-highdata\}.
