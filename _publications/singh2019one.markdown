---
layout: publication
title: One Embedding To Do Them All
authors: Singh Loveperteek, Singh Shreya, Arora Sagar, Borar Sumit
conference: Arxiv
year: 2019
bibkey: singh2019one
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.12120'}]
tags: ["Tools-&-Libraries", "Evaluation"]
short_authors: Singh et al.
---
Online shopping caters to the needs of millions of users daily. Search,
recommendations, personalization have become essential building blocks for
serving customer needs. Efficacy of such systems is dependent on a thorough
understanding of products and their representation. Multiple information
sources and data types provide a complete picture of the product on the
platform. While each of these tasks shares some common characteristics,
typically product embeddings are trained and used in isolation.
  In this paper, we propose a framework to combine multiple data sources and
learn unified embeddings for products on our e-commerce platform. Our product
embeddings are built from three types of data sources - catalog text data, a
user's clickstream session data and product images. We use various techniques
like denoising auto-encoders for text, Bayesian personalized ranking (BPR) for
clickstream data, Siamese neural network architecture for image data and
combined ensemble over the above methods for unified embeddings. Further, we
compare and analyze the performance of these embeddings across three unrelated
real-world e-commerce tasks specifically checking product attribute coverage,
finding similar products and predicting returns. We show that unified product
embeddings perform uniformly well across all these tasks.