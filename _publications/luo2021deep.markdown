---
layout: publication
title: Deep Unsupervised Hashing By Distilled Smooth Guidance
authors: Luo Xiao, Ma Zeyu, Wu Daqing, Zhong Huasong, Chen Chong, Ma Jinwen, Deng Minghua
conference: "ICME"
year: 2021
bibkey: luo2021deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2105.06125"}
tags: ['ICME', 'Unsupervised']
---
Hashing has been widely used in approximate nearest neighbor search for its storage and computational efficiency. Deep supervised hashing methods are not widely used because of the lack of labeled data especially when the domain is transferred. Meanwhile unsupervised deep hashing models can hardly achieve satisfactory performance due to the lack of reliable similarity signals. To tackle this problem we propose a novel deep unsupervised hashing method namely Distilled Smooth Guidance (DSG) which can learn a distilled dataset consisting of similarity signals as well as smooth confidence signals. To be specific we obtain the similarity confidence weights based on the initial noisy similarity signals learned from local structures and construct a priority loss function for smooth similarity-preserving learning. Besides global information based on clustering is utilized to distill the image pairs by removing contradictory similarity signals. Extensive experiments on three widely used benchmark datasets show that the proposed DSG consistently outperforms the state-of-the-art search methods.
