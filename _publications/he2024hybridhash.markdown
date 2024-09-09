---
layout: publication
title: "HybridHash: Hybrid Convolutional and Self-Attention Deep Hashing for Image Retrieval"
authors: He Chao, Wei Hongxi
conference: Arxiv
year: 2024
bibkey: he2024hybridhash
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/2405.07524"}
  - {name: "Code", url: "https://github.com/shuaichaochao/HybridHash."}
tags: ['ARXIV', 'Image Retrieval']
---
Deep image hashing aims to map input images into simple binary hash codes via deep neural networks and thus enable effective large-scale image retrieval. Recently, hybrid networks that combine convolution and Transformer have achieved superior performance on various computer tasks and have attracted extensive attention from researchers. Nevertheless, the potential benefits of such hybrid networks in image retrieval still need to be verified. To this end, we propose a hybrid convolutional and self-attention deep hashing method known as HybridHash. Specifically, we propose a backbone network with stage-wise architecture in which the block aggregation function is introduced to achieve the effect of local self-attention and reduce the computational complexity. The interaction module has been elaborately designed to promote the communication of information between image blocks and to enhance the visual representations. We have conducted comprehensive experiments on three widely used datasets: CIFAR-10, NUS-WIDE and IMAGENET. The experimental results demonstrate that the method proposed in this paper has superior performance with respect to state-of-the-art deep hashing methods. Source code is available https://github.com/shuaichaochao/HybridHash.