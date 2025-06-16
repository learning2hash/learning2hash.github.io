---
layout: publication
title: Towards Optimal Deep Hashing Via Policy Gradient
authors: Yuan Xin, Ren, Lu, Zhou
conference: Arxiv
year: 2024
citations: 0
bibkey: yuan2024towards
additional_links: [{name: Paper, url: 'https://openaccess.thecvf.com/content_ECCV_2018/papers/Xin_Yuan_Towards_Optimal_Deep_ECCV_2018_paper.pdf'}]
tags: [Deep Hashing, ANN Search, Evaluation Metrics, Benchmarks and Datasets]
---
In this paper, we propose a simple yet effective relaxation free method to learn more effective binary codes via policy gradient for
scalable image search. While a variety of deep hashing methods have been
proposed in recent years, most of them are confronted by the dilemma
to obtain optimal binary codes in a truly end-to-end manner with nonsmooth sign activations. Unlike existing methods which usually employ a
general relaxation framework to adapt to the gradient-based algorithms,
our approach formulates the non-smooth part of the hashing network
as sampling with a stochastic policy, so that the retrieval performance
degradation caused by the relaxation can be avoided. Specifically, our
method directly generates the binary codes and maximizes the expectation of rewards for similarity preservation, where the network can be
trained directly via policy gradient. Hence, the differentiation challenge
for discrete optimization can be naturally addressed, which leads to effective gradients and binary codes. Extensive experimental results on three
benchmark datasets validate the effectiveness of the proposed method.