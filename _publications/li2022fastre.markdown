---
layout: publication
title: 'Fastre: Towards Fast Relation Extraction With Convolutional Encoder And Improved
  Cascade Binary Tagging Framework'
authors: Guozheng Li, Xu Chen, Peng Wang, Jiafeng Xie, Qiqing Luo
conference: Arxiv
year: 2022
bibkey: li2022fastre
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.02490'}]
tags: ["Efficiency"]
short_authors: Li et al.
---
Recent work for extracting relations from texts has achieved excellent
performance. However, most existing methods pay less attention to the
efficiency, making it still challenging to quickly extract relations from
massive or streaming text data in realistic scenarios. The main efficiency
bottleneck is that these methods use a Transformer-based pre-trained language
model for encoding, which heavily affects the training speed and inference
speed. To address this issue, we propose a fast relation extraction model
(FastRE) based on convolutional encoder and improved cascade binary tagging
framework. Compared to previous work, FastRE employs several innovations to
improve efficiency while also keeping promising performance. Concretely, FastRE
adopts a novel convolutional encoder architecture combined with dilated
convolution, gated unit and residual connection, which significantly reduces
the computation cost of training and inference, while maintaining the
satisfactory performance. Moreover, to improve the cascade binary tagging
framework, FastRE first introduces a type-relation mapping mechanism to
accelerate tagging efficiency and alleviate relation redundancy, and then
utilizes a position-dependent adaptive thresholding strategy to obtain higher
tagging accuracy and better model generalization. Experimental results
demonstrate that FastRE is well balanced between efficiency and performance,
and achieves 3-10x training speed, 7-15x inference speed faster, and 1/100
parameters compared to the state-of-the-art models, while the performance is
still competitive.