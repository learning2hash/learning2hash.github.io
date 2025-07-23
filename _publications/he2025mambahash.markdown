---
layout: publication
title: 'Mambahash: Visual State Space Deep Hashing Model For Large-scale Image Retrieval'
authors: He Chao, Wei Hongxi
conference: Proceedings of the 2025 International Conference on Multimedia Retrieval
year: 2025
bibkey: he2025mambahash
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.16353'}]
tags: ["Efficiency", "Evaluation", "Hashing Methods", "Image Retrieval", "Neural Hashing", "Scalability"]
short_authors: He Chao, Wei Hongxi
---
Deep image hashing aims to enable effective large-scale image retrieval by mapping the input images into simple binary hash codes through deep neural networks. More recently, Vision Mamba with linear time complexity has attracted extensive attention from researchers by achieving outstanding performance on various computer tasks. Nevertheless, the suitability of Mamba for large-scale image retrieval tasks still needs to be explored. Towards this end, we propose a visual state space hashing model, called MambaHash. Concretely, we propose a backbone network with stage-wise architecture, in which grouped Mamba operation is introduced to model local and global information by utilizing Mamba to perform multi-directional scanning along different groups of the channel. Subsequently, the proposed channel interaction attention module is used to enhance information communication across channels. Finally, we meticulously design an adaptive feature enhancement module to increase feature diversity and enhance the visual representation capability of the model. We have conducted comprehensive experiments on three widely used datasets: CIFAR-10, NUS-WIDE and IMAGENET. The experimental results demonstrate that compared with the state-of-the-art deep hashing methods, our proposed MambaHash has well efficiency and superior performance to effectively accomplish large-scale image retrieval tasks. Source code is available https://github.com/shuaichaochao/MambaHash.git