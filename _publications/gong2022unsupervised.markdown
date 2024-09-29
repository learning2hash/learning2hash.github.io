---
layout: publication
title: Vit2hash Unsupervised Information45;preserving Hashing
authors: Gong Qinkang, Wang Liangdao, Lai Hanjiang, Pan Yan, Yin Jian
conference: "Arxiv"
year: 2022
bibkey: gong2022unsupervised
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2201.05541"}
tags: ['ARXIV', 'Quantisation', 'Unsupervised']
---
Unsupervised image hashing which maps images into binary codes without supervision is a compressor with a high compression rate. Hence how to preserving meaningful information of the original data is a critical problem. Inspired by the large45;scale vision pre45;training model known as ViT which has shown significant progress for learning visual representations in this paper we propose a simple information45;preserving compressor to finetune the ViT model for the target unsupervised hashing task. Specifically from pixels to continuous features we first propose a feature45;preserving module using the corrupted image as input to reconstruct the original feature from the pre45;trained ViT model and the complete image so that the feature extractor can focus on preserving the meaningful information of original data. Secondly from continuous features to hash codes we propose a hashing45;preserving module which aims to keep the semantic information from the pre45;trained ViT model by using the proposed Kullback45;Leibler divergence loss. Besides the quantization loss and the similarity loss are added to minimize the quantization error. Our method is very simple and achieves a significantly higher degree of MAP on three benchmark image datasets.
