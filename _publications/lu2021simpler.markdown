---
layout: publication
title: 'Simpler Is Better: Few-shot Semantic Segmentation With Classifier Weight Transformer'
authors: Zhihe Lu, Sen He, Xiatian Zhu, Li Zhang, Yi-Zhe Song, Tao Xiang
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: lu2021simpler
citations: 155
additional_links: [{name: Code, url: 'https://github.com/zhiheLu/CWT-for-FSS'}, {
    name: Paper, url: 'https://arxiv.org/abs/2108.03032'}]
tags: ["Few Shot & Zero Shot", "ICCV"]
short_authors: Lu et al.
---
A few-shot semantic segmentation model is typically composed of a CNN
encoder, a CNN decoder and a simple classifier (separating foreground and
background pixels). Most existing methods meta-learn all three model components
for fast adaptation to a new class. However, given that as few as a single
support set image is available, effective model adaption of all three
components to the new class is extremely challenging. In this work we propose
to simplify the meta-learning task by focusing solely on the simplest
component, the classifier, whilst leaving the encoder and decoder to
pre-training. We hypothesize that if we pre-train an off-the-shelf segmentation
model over a set of diverse training classes with sufficient annotations, the
encoder and decoder can capture rich discriminative features applicable for any
unseen classes, rendering the subsequent meta-learning stage unnecessary. For
the classifier meta-learning, we introduce a Classifier Weight Transformer
(CWT) designed to dynamically adapt the supportset trained classifier's weights
to each query image in an inductive way. Extensive experiments on two standard
benchmarks show that despite its simplicity, our method outperforms the
state-of-the-art alternatives, often by a large margin.Code is available on
https://github.com/zhiheLu/CWT-for-FSS.