---
layout: publication
title: 'Video And Audio Are Images: A Cross-modal Mixer For Original Data On Video-audio
  Retrieval'
authors: Zichen Yuan, Qi Shen, Bingyi Zheng, Yuting Liu, Linying Jiang, Guibing Guo
conference: Arxiv
year: 2023
bibkey: yuan2023video
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.13820'}]
tags: [Video Retrieval, Evaluation, Datasets, Multimodal Retrieval, Tools & Libraries,
  Audio Retrieval]
short_authors: Yuan et al.
---
Cross-modal retrieval has become popular in recent years, particularly with
the rise of multimedia. Generally, the information from each modality exhibits
distinct representations and semantic information, which makes feature tends to
be in separate latent spaces encoded with dual-tower architecture and makes it
difficult to establish semantic relationships between modalities, resulting in
poor retrieval performance. To address this issue, we propose a novel framework
for cross-modal retrieval which consists of a cross-modal mixer, a masked
autoencoder for pre-training, and a cross-modal retriever for downstream
tasks.In specific, we first adopt cross-modal mixer and mask modeling to fuse
the original modality and eliminate redundancy. Then, an encoder-decoder
architecture is applied to achieve a fuse-then-separate task in the
pre-training phase.We feed masked fused representations into the encoder and
reconstruct them with the decoder, ultimately separating the original data of
two modalities. In downstream tasks, we use the pre-trained encoder to build
the cross-modal retrieval method. Extensive experiments on 2 real-world
datasets show that our approach outperforms previous state-of-the-art methods
in video-audio matching tasks, improving retrieval accuracy by up to 2 times.
Furthermore, we prove our model performance by transferring it to other
downstream tasks as a universal model.