---
layout: publication
title: Spectral Clustering For Discrete Distributions
authors: Zixiao Wang, Dong Qiao, Jicong Fan
conference: Arxiv
year: 2024
bibkey: wang2024spectral
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.13913'}]
tags: []
short_authors: Zixiao Wang, Dong Qiao, Jicong Fan
---
The discrete distribution is often used to describe complex instances in
machine learning, such as images, sequences, and documents. Traditionally,
clustering of discrete distributions (D2C) has been approached using
Wasserstein barycenter methods. These methods operate under the assumption that
clusters can be well-represented by barycenters, which is seldom true in many
real-world applications. Additionally, these methods are not scalable for large
datasets due to the high computational cost of calculating Wasserstein
barycenters. In this work, we explore the feasibility of using spectral
clustering combined with distribution affinity measures (e.g., maximum mean
discrepancy and Wasserstein distance) to cluster discrete distributions. We
demonstrate that these methods can be more accurate and efficient than
barycenter methods. To further enhance scalability, we propose using linear
optimal transport to construct affinity matrices efficiently for large
datasets. We provide theoretical guarantees for the success of our methods in
clustering distributions. Experiments on both synthetic and real data show that
our methods outperform existing baselines.