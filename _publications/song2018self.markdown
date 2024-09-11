---
layout: publication
title: "Self-Supervised Video Hashing with Hierarchical Binary Auto-encoder"
authors: Jingkuan Song, Hanwang Zhang, Xiangpeng Li, Lianli Gao, Meng Wang, Richang Hong
conference: TIP
year: 2018
bibkey: song2018self
additional_links:
   - {name: "PDF", url: "https://arxiv.org/abs/1802.02305"}
tags: ["Self-Supervised", "Video Retrieval", "TIP"]
---
Existing video hash functions are built on three isolated stages: frame pooling, relaxed learning, and binarization, which have not adequately explored the temporal order of video frames in a joint binary optimization model, resulting in severe information loss. In this paper, we propose a novel unsupervised video hashing framework dubbed Self-Supervised Video Hashing (SSVH), that is able to capture the temporal nature of videos in an end-to-end learning-to-hash fashion. We specifically address two central problems: 1) how to design an encoder-decoder architecture to generate binary codes for videos; and 2) how to equip the binary codes with the ability of accurate video retrieval. We design a hierarchical binary autoencoder to model the temporal dependencies in videos with multiple granularities, and embed the videos into binary codes with less computations than the stacked architecture. Then, we encourage the binary codes to simultaneously reconstruct the visual content and neighborhood structure of the videos. Experiments on two real-world datasets (FCVID and YFCC) show that our SSVH method can significantly outperform the state-of-the-art methods and achieve the currently best performance on the task of unsupervised video retrieval.
