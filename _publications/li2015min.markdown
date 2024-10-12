---
layout: publication
title: Min-max Kernels
authors: Li Ping
conference: "Arxiv"
year: 2015
bibkey: li2015min
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1503.01737"}
tags: ['ARXIV', 'Supervised']
---
The min-max kernel is a generalization of the popular resemblance kernel (which is designed for binary data). In this paper, we demonstrate, through an extensive classification study using kernel machines, that the min-max kernel often provides an effective measure of similarity for nonnegative data. As the min-max kernel is nonlinear and might be difficult to be used for industrial applications with massive data, we show that the min-max kernel can be linearized via hashing techniques. This allows practitioners to apply min-max kernel to large-scale applications using well matured linear algorithms such as linear SVM or logistic regression. The previous remarkable work on consistent weighted sampling (CWS) produces samples in the form of (\\(i^*, t^*\\)) where the \\(i^*\\) records the location (and in fact also the weights) information analogous to the samples produced by classical minwise hashing on binary data. Because the \\(t^*\\) is theoretically unbounded, it was not immediately clear how to effectively implement CWS for building large-scale linear classifiers. In this paper, we provide a simple solution by discarding \\(t^*\\) (which we refer to as the 0-bit scheme). Via an extensive empirical study, we show that this 0-bit scheme does not lose essential information. We then apply the 0-bit CWS for building linear classifiers to approximate min-max kernel classifiers, as extensively validated on a wide range of publicly available classification datasets. We expect this work will generate interests among data mining practitioners who would like to efficiently utilize the nonlinear information of non-binary and nonnegative data.
