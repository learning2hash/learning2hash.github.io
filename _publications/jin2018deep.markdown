---
layout: publication
title: "Deep Saliency Hashing"
authors: Jin Sheng, Yao Hongxun, Sun Xiaoshuai, Zhou Shangchen, Zhang Lei, Hua Xiansheng
conference: Arxiv
year: 2018
bibkey: jin2018deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1807.01459"}
tags: ['ARXIV', 'Quantisation', 'TOM']
---
In recent years, hashing methods have been proved to be effective and efficient for the large-scale Web media search. However, the existing general hashing methods have limited discriminative power for describing fine-grained objects that share similar overall appearance but have subtle difference. To solve this problem, we for the first time introduce the attention mechanism to the learning of fine-grained hashing codes. Specifically, we propose a novel deep hashing model, named deep saliency hashing (DSaH), which automatically mines salient regions and learns semantic-preserving hashing codes simultaneously. DSaH is a two-step end-to-end model consisting of an attention network and a hashing network. Our loss function contains three basic components, including the semantic loss, the saliency loss, and the quantization loss. As the core of DSaH, the saliency loss guides the attention network to mine discriminative regions from pairs of images. We conduct extensive experiments on both fine-grained and general retrieval datasets for performance evaluation. Experimental results on fine-grained datasets, including Oxford Flowers-17, Stanford Dogs-120, and CUB Bird demonstrate that our DSaH performs the best for fine-grained retrieval task and beats the strongest competitor (DTQ) by approximately 10% on both Stanford Dogs-120 and CUB Bird. DSaH is also comparable to several state-of-the-art hashing methods on general datasets, including CIFAR-10 and NUS-WIDE.