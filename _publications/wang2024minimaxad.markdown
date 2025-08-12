---
layout: publication
title: 'Minimaxad: A Lightweight Autoencoder For Feature-rich Anomaly Detection'
authors: Fengjie Wang, Chengming Liu, Lei Shi, Pang Haibo
conference: Computers in Industry
year: 2025
bibkey: wang2024minimaxad
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.09933'}]
tags: []
short_authors: Wang et al.
---
Previous industrial anomaly detection methods often struggle to handle the extensive diversity in training sets, particularly when they contain stylistically diverse and feature-rich samples, which we categorize as feature-rich anomaly detection datasets (FRADs). This challenge is evident in applications such as multi-view and multi-class scenarios. To address this challenge, we developed MiniMaxAD, a efficient autoencoder designed to efficiently compress and memorize extensive information from normal images. Our model employs a technique that enhances feature diversity, thereby increasing the effective capacity of the network. It also utilizes large kernel convolution to extract highly abstract patterns, which contribute to efficient and compact feature embedding. Moreover, we introduce an Adaptive Contraction Hard Mining Loss (ADCLoss), specifically tailored to FRADs. In our methodology, any dataset can be unified under the framework of feature-rich anomaly detection, in a way that the benefits far outweigh the drawbacks. Our approach has achieved state-of-the-art performance in multiple challenging benchmarks. Code is available at: \href\{https://github.com/WangFengJiee/MiniMaxAD\}\{https://github.com/WangFengJiee/MiniMaxAD\}