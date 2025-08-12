---
layout: publication
title: Learning With Neighbor Consistency For Noisy Labels
authors: Ahmet Iscen, Jack Valmadre, Anurag Arnab, Cordelia Schmid
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: iscen2022learning
citations: 60
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.02200'}]
tags: ["CVPR"]
short_authors: Iscen et al.
---
Recent advances in deep learning have relied on large, labelled datasets to
train high-capacity models. However, collecting large datasets in a time- and
cost-efficient manner often results in label noise. We present a method for
learning from noisy labels that leverages similarities between training
examples in feature space, encouraging the prediction of each example to be
similar to its nearest neighbours. Compared to training algorithms that use
multiple models or distinct stages, our approach takes the form of a simple,
additional regularization term. It can be interpreted as an inductive version
of the classical, transductive label propagation algorithm. We thoroughly
evaluate our method on datasets evaluating both synthetic (CIFAR-10, CIFAR-100)
and realistic (mini-WebVision, WebVision, Clothing1M, mini-ImageNet-Red) noise,
and achieve competitive or state-of-the-art accuracies across all of them.