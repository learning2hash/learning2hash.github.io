---
layout: publication
title: Few-shot Object Detection Via Variational Feature Aggregation
authors: Jiaming Han, Yuqiang Ren, Jian Ding, Ke Yan, Gui-Song Xia
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2023
bibkey: han2023few
citations: 55
additional_links: [{name: Code, url: 'https://github.com/csuhan/VFA'}, {name: Paper,
    url: 'https://arxiv.org/abs/2301.13411'}]
tags: ["AAAI", "Few Shot & Zero Shot"]
short_authors: Han et al.
---
As few-shot object detectors are often trained with abundant base samples and
fine-tuned on few-shot novel examples,the learned models are usually biased to
base classes and sensitive to the variance of novel examples. To address this
issue, we propose a meta-learning framework with two novel feature aggregation
schemes. More precisely, we first present a Class-Agnostic Aggregation (CAA)
method, where the query and support features can be aggregated regardless of
their categories. The interactions between different classes encourage
class-agnostic representations and reduce confusion between base and novel
classes. Based on the CAA, we then propose a Variational Feature Aggregation
(VFA) method, which encodes support examples into class-level support features
for robust feature aggregation. We use a variational autoencoder to estimate
class distributions and sample variational features from distributions that are
more robust to the variance of support examples. Besides, we decouple
classification and regression tasks so that VFA is performed on the
classification branch without affecting object localization. Extensive
experiments on PASCAL VOC and COCO demonstrate that our method significantly
outperforms a strong baseline (up to 16%) and previous state-of-the-art
methods (4% in average). Code will be available at:
https://github.com/csuhan/VFA