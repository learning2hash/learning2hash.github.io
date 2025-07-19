---
layout: publication
title: Adaptive Training of Random Mapping for Data Quantization
authors: Cheng Miao, Tsoi Ah Chung
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2016
bibkey: cheng2016adaptive
citations: 36
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1606.08808'}]
tags: [Quantization, Evaluation, CVPR]
---
Data quantization learns encoding results of data with certain requirements,
and provides a broad perspective of many real-world applications to data
handling. Nevertheless, the results of encoder is usually limited to
multivariate inputs with the random mapping, and side information of binary
codes are hardly to mostly depict the original data patterns as possible. In
the literature, cosine based random quantization has attracted much attentions
due to its intrinsic bounded results. Nevertheless, it usually suffers from the
uncertain outputs, and information of original data fails to be fully preserved
in the reduced codes. In this work, a novel binary embedding method, termed
adaptive training quantization (ATQ), is proposed to learn the ideal transform
of random encoder, where the limitation of cosine random mapping is tackled. As
an adaptive learning idea, the reduced mapping is adaptively calculated with
idea of data group, while the bias of random transform is to be improved to
hold most matching information. Experimental results show that the proposed
method is able to obtain outstanding performance compared with other random
quantization methods.