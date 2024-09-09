---
layout: publication
title: "Vision Transformer Hashing for Image Retrieval"
authors: Dubey Shiv Ram, Singh Satish Kumar, Chu Wei-Ta
conference: Arxiv
year: 2021
bibkey: dubey2021vision
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/2109.12564"}
  - {name: "Code", url: "https://github.com/shivram1987/VisionTransformerHashing}."}
tags: ['ARXIV', 'Deep Learning', 'Image Retrieval', 'Quantisation', 'Supervised']
---
Deep learning has shown a tremendous growth in hashing techniques for image retrieval. Recently, Transformer has emerged as a new architecture by utilizing self-attention without convolution. Transformer is also extended to Vision Transformer (ViT) for the visual recognition with a promising performance on ImageNet. In this paper, we propose a Vision Transformer based Hashing (VTS) for image retrieval. We utilize the pre-trained ViT on ImageNet as the backbone network and add the hashing head. The proposed VTS model is fine tuned for hashing under six different image retrieval frameworks, including Deep Supervised Hashing (DSH), HashNet, GreedyHash, Improved Deep Hashing Network (IDHN), Deep Polarized Network (DPN) and Central Similarity Quantization (CSQ) with their objective functions. We perform the extensive experiments on CIFAR10, ImageNet, NUS-Wide, and COCO datasets. The proposed VTS based image retrieval outperforms the recent state-of-the-art hashing techniques with a great margin. We also find the proposed VTS model as the backbone network is better than the existing networks, such as AlexNet and ResNet. The code is released at \url{https://github.com/shivram1987/VisionTransformerHashing}.