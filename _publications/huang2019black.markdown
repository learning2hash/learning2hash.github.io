---
layout: publication
title: Black-box Adversarial Attack With Transferable Model-based Embedding
authors: Zhichao Huang, Tong Zhang
conference: Arxiv
year: 2019
bibkey: huang2019black
citations: 49
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.07140'}]
tags: ["Efficiency", "Robustness", "Tools & Libraries"]
short_authors: Zhichao Huang, Tong Zhang
---
We present a new method for black-box adversarial attack. Unlike previous
methods that combined transfer-based and scored-based methods by using the
gradient or initialization of a surrogate white-box model, this new method
tries to learn a low-dimensional embedding using a pretrained model, and then
performs efficient search within the embedding space to attack an unknown
target network. The method produces adversarial perturbations with high level
semantic patterns that are easily transferable. We show that this approach can
greatly improve the query efficiency of black-box adversarial attack across
different target network architectures. We evaluate our approach on MNIST,
ImageNet and Google Cloud Vision API, resulting in a significant reduction on
the number of queries. We also attack adversarially defended networks on
CIFAR10 and ImageNet, where our method not only reduces the number of queries,
but also improves the attack success rate.