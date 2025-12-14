---
layout: publication
title: Improved Mix-up With Kl-entropy For Learning From Noisy Labels
authors: Qian Zhang, Feifei Lee, Ya-Gang Wang, Qiu Chen
conference: Arxiv
year: 2019
bibkey: zhang2019improved
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.05488'}]
tags: [Evaluation, Tools & Libraries, Datasets]
short_authors: Zhang et al.
---
Despite the deep neural networks (DNN) has achieved excellent performance in
image classification researches, the training of DNNs needs a large of clean
data with accurate annotations. The collect of a dataset is easy, but it is
difficult to annotate the collecting data. On the websites, there exist a lot
of image data which contains inaccurate annotations, but training on these
datasets may make networks easier to over-fit the noisy labels and cause
performance degradation. In this work, we propose an improved joint
optimization framework, which mixed the mix-up entropy and Kullback-Leibler
(KL) entropy as the loss function. The new loss function can give the better
fine-tuning after the framework updates both the label annotations. We conduct
experiments on CIFAR-10 dataset and Clothing1M dataset. The result shows the
advantageous performance of our approach compared with other state-of-the-art
methods.