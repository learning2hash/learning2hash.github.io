---
layout: publication
title: Attention-based Saliency Hashing for Ophthalmic Image Retrieval
authors: Fang Jiansheng, Xu Yanwu, Zhang Xiaoqing, Hu Yan, Liu Jiang
conference: "Arxiv"
year: 2020
bibkey: fang2020attention
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2012.03466"}
tags: ['ARXIV', 'Image Retrieval']
---
Deep hashing methods have been proved to be effective for the large-scale medical image search assisting reference-based diagnosis for clinicians. However when the salient region plays a maximal discriminative role in ophthalmic image existing deep hashing methods do not fully exploit the learning ability of the deep network to capture the features of salient regions pointedly. The different grades or classes of ophthalmic images may be share similar overall performance but have subtle differences that can be differentiated by mining salient regions. To address this issue we propose a novel end-to-end network named Attention-based Saliency Hashing (ASH) for learning compact hash-code to represent ophthalmic images. ASH embeds a spatial-attention module to focus more on the representation of salient regions and highlights their essential role in differentiating ophthalmic images. Benefiting from the spatial-attention module the information of salient regions can be mapped into the hash-code for similarity calculation. In the training stage we input the image pairs to share the weights of the network and a pairwise loss is designed to maximize the discriminability of the hash-code. In the retrieval stage ASH obtains the hash-code by inputting an image with an end-to-end manner then the hash-code is used to similarity calculation to return the most similar images. Extensive experiments on two different modalities of ophthalmic image datasets demonstrate that the proposed ASH can further improve the retrieval performance compared to the state-of-the-art deep hashing methods due to the huge contributions of the spatial-attention module.
