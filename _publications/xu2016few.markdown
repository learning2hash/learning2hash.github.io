---
layout: publication
title: Few-shot Object Recognition From Machine-labeled Web Images
authors: Zhongwen Xu, Linchao Zhu, Yi Yang
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: xu2016few
citations: 64
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.06152'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Zhongwen Xu, Linchao Zhu, Yi Yang
---
With the tremendous advances of Convolutional Neural Networks (ConvNets) on
object recognition, we can now obtain reliable enough machine-labeled
annotations easily by predictions from off-the-shelf ConvNets. In this work, we
present an abstraction memory based framework for few-shot learning, building
upon machine-labeled image annotations. Our method takes some large-scale
machine-annotated datasets (e.g., OpenImages) as an external memory bank. In
the external memory bank, the information is stored in the memory slots with
the form of key-value, where image feature is regarded as key and label
embedding serves as value. When queried by the few-shot examples, our model
selects visually similar data from the external memory bank, and writes the
useful information obtained from related external data into another memory
bank, i.e., abstraction memory. Long Short-Term Memory (LSTM) controllers and
attention mechanisms are utilized to guarantee the data written to the
abstraction memory is correlated to the query example. The abstraction memory
concentrates information from the external memory bank, so that it makes the
few-shot recognition effective. In the experiments, we firstly confirm that our
model can learn to conduct few-shot object recognition on clean human-labeled
data from ImageNet dataset. Then, we demonstrate that with our model,
machine-labeled image annotations are very effective and abundant resources to
perform object recognition on novel categories. Experimental results show that
our proposed model with machine-labeled annotations achieves great performance,
only with a gap of 1% between of the one with human-labeled annotations.