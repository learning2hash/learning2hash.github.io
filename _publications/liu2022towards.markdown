---
layout: publication
title: Towards Fast And Accurate Federated Learning With Non-iid Data For Cloud-based
  Iot Applications
authors: Tian Liu, Jiahao Ding, Ting Wang, Miao Pan, Mingsong Chen
conference: Journal of Circuits, Systems and Computers
year: 2022
bibkey: liu2022towards
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.12515'}]
tags: ["Evaluation", "Locality-Sensitive-Hashing", "Privacy & Security"]
short_authors: Liu et al.
---
As a promising method of central model training on decentralized device data
while securing user privacy, Federated Learning (FL)is becoming popular in
Internet of Things (IoT) design. However, when the data collected by IoT
devices are highly skewed in a non-independent and identically distributed
(non-IID) manner, the accuracy of vanilla FL method cannot be guaranteed.
Although there exist various solutions that try to address the bottleneck of FL
with non-IID data, most of them suffer from extra intolerable communication
overhead and low model accuracy. To enable fast and accurate FL, this paper
proposes a novel data-based device grouping approach that can effectively
reduce the disadvantages of weight divergence during the training of non-IID
data. However, since our grouping method is based on the similarity of
extracted feature maps from IoT devices, it may incur additional risks of
privacy exposure. To solve this problem, we propose an improved version by
exploiting similarity information using the Locality-Sensitive Hashing (LSH)
algorithm without exposing extracted feature maps. Comprehensive experimental
results on well-known benchmarks show that our approach can not only accelerate
the convergence rate, but also improve the prediction accuracy for FL with
non-IID data.