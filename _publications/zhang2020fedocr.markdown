---
layout: publication
title: Fedocr Communication-efficient Federated Learning For Scene Text Recognition
authors: Zhang Wenqing, Qiu Yang, Bai Song, Zhang Rui, Wei Xiaolin, Bai Xiang
conference: "Arxiv"
year: 2020
bibkey: zhang2020fedocr
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2007.11462"}
tags: ['ARXIV', 'Supervised']
---
While scene text recognition techniques have been widely used in commercial applications, data privacy has rarely been taken into account by this research community. Most existing algorithms have assumed a set of shared or centralized training data. However, in practice, data may be distributed on different local devices that can not be centralized to share due to the privacy restrictions. In this paper, we study how to make use of decentralized datasets for training a robust scene text recognizer while keeping them stay on local devices. To the best of our knowledge, we propose the first framework leveraging federated learning for scene text recognition, which is trained with decentralized datasets collaboratively. Hence we name it FedOCR. To make FedCOR fairly suitable to be deployed on end devices, we make two improvements including using lightweight models and hashing techniques. We argue that both are crucial for FedOCR in terms of the communication efficiency of federated learning. The simulations on decentralized datasets show that the proposed FedOCR achieves competitive results to the models that are trained with centralized data, with fewer communication costs and higher-level privacy-preserving.
