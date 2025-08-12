---
layout: publication
title: Deep Kernels With Probabilistic Embeddings For Small-data Learning
authors: Ankur Mallick, Chaitanya Dwivedi, Bhavya Kailkhura, Gauri Joshi, T. Yong-jin
  Han
conference: Arxiv
year: 2021
bibkey: mallick2019deep
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.05858'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Mallick et al.
---
Gaussian Processes (GPs) are known to provide accurate predictions and
uncertainty estimates even with small amounts of labeled data by capturing
similarity between data points through their kernel function. However
traditional GP kernels are not very effective at capturing similarity between
high dimensional data points. Neural networks can be used to learn good
representations that encode intricate structures in high dimensional data, and
can be used as inputs to the GP kernel. However the huge data requirement of
neural networks makes this approach ineffective in small data settings. To
solves the conflicting problems of representation learning and data efficiency,
we propose to learn deep kernels on probabilistic embeddings by using a
probabilistic neural network. Our approach maps high-dimensional data to a
probability distribution in a low dimensional subspace and then computes a
kernel between these distributions to capture similarity. To enable end-to-end
learning, we derive a functional gradient descent procedure for training the
model. Experiments on a variety of datasets show that our approach outperforms
the state-of-the-art in GP kernel learning in both supervised and
semi-supervised settings. We also extend our approach to other small-data
paradigms such as few-shot classification where it outperforms previous
approaches on mini-Imagenet and CUB datasets.