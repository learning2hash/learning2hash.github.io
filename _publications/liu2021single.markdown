---
layout: publication
title: Single-path Bit Sharing For Automatic Loss-aware Model Compression
authors: Jing Liu, Bohan Zhuang, Peng Chen, Chunhua Shen, Jianfei Cai, Mingkui Tan
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2023
bibkey: liu2021single
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.04935'}]
tags: ["Quantization"]
short_authors: Liu et al.
---
Network pruning and quantization are proven to be effective ways for deep
model compression. To obtain a highly compact model, most methods first perform
network pruning and then conduct network quantization based on the pruned
model. However, this strategy may ignore that they would affect each other and
thus performing them separately may lead to sub-optimal performance. To address
this, performing pruning and quantization jointly is essential. Nevertheless,
how to make a trade-off between pruning and quantization is non-trivial.
Moreover, existing compression methods often rely on some pre-defined
compression configurations. Some attempts have been made to search for optimal
configurations, which however may take unbearable optimization cost. To address
the above issues, we devise a simple yet effective method named Single-path Bit
Sharing (SBS). Specifically, we first consider network pruning as a special
case of quantization, which provides a unified view for pruning and
quantization. We then introduce a single-path model to encode all candidate
compression configurations. In this way, the configuration search problem is
transformed into a subset selection problem, which significantly reduces the
number of parameters, computational cost and optimization difficulty. Relying
on the single-path model, we further introduce learnable binary gates to encode
the choice of bitwidth. By jointly training the binary gates in conjunction
with network parameters, the compression configurations of each layer can be
automatically determined. Extensive experiments on both CIFAR-100 and ImageNet
show that SBS is able to significantly reduce computational cost while
achieving promising performance. For example, our SBS compressed MobileNetV2
achieves 22.6x Bit-Operation (BOP) reduction with only 0.1% drop in the Top-1
accuracy.