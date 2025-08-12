---
layout: publication
title: Deep Learning Recommendation Model For Personalization And Recommendation Systems
authors: Maxim Naumov, Dheevatsa Mudigere, Hao-Jun Michael Shi, Jianyu Huang, Narayanan
  Sundaraman, Jongsoo Park, Xiaodong Wang, Udit Gupta, Carole-Jean Wu, Alisson G.
  Azzolini, Dmytro Dzhulgakov, Andrey Mallevich, Ilia Cherniavskii, Yinghai Lu, Raghuraman
  Krishnamoorthi, Ansha Yu, Volodymyr Kondratenko, Stephanie Pereira, Xianjie Chen,
  Wenlin Chen, Vijay Rao, Bill Jia, Liang Xiong, Misha Smelyanskiy
conference: Arxiv
year: 2019
bibkey: naumov2019deep
citations: 339
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.00091'}]
tags: ["Recommender Systems"]
short_authors: Naumov et al.
---
With the advent of deep learning, neural network-based recommendation models
have emerged as an important tool for tackling personalization and
recommendation tasks. These networks differ significantly from other deep
learning networks due to their need to handle categorical features and are not
well studied or understood. In this paper, we develop a state-of-the-art deep
learning recommendation model (DLRM) and provide its implementation in both
PyTorch and Caffe2 frameworks. In addition, we design a specialized
parallelization scheme utilizing model parallelism on the embedding tables to
mitigate memory constraints while exploiting data parallelism to scale-out
compute from the fully-connected layers. We compare DLRM against existing
recommendation models and characterize its performance on the Big Basin AI
platform, demonstrating its usefulness as a benchmark for future algorithmic
experimentation and system co-design.