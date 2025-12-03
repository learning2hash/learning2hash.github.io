---
layout: publication
title: Adaptive Loss-aware Quantization For Multi-bit Networks
authors: Zhongnan Qu, Zimu Zhou, Yun Cheng, Lothar Thiele
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: qu2019adaptive
citations: 47
additional_links: [{name: Code, url: 'https://github.com/zqu1992/ALQ'}, {name: Paper,
    url: 'https://arxiv.org/abs/1912.08883'}]
tags: ["CVPR", "Datasets", "Evaluation", "Quantization"]
short_authors: Qu et al.
---
We investigate the compression of deep neural networks by quantizing their
weights and activations into multiple binary bases, known as multi-bit networks
(MBNs), which accelerate the inference and reduce the storage for the
deployment on low-resource mobile and embedded platforms. We propose Adaptive
Loss-aware Quantization (ALQ), a new MBN quantization pipeline that is able to
achieve an average bitwidth below one-bit without notable loss in inference
accuracy. Unlike previous MBN quantization solutions that train a quantizer by
minimizing the error to reconstruct full precision weights, ALQ directly
minimizes the quantization-induced error on the loss function involving neither
gradient approximation nor full precision maintenance. ALQ also exploits
strategies including adaptive bitwidth, smooth bitwidth reduction, and
iterative trained quantization to allow a smaller network size without loss in
accuracy. Experiment results on popular image datasets show that ALQ
outperforms state-of-the-art compressed networks in terms of both storage and
accuracy. Code is available at https://github.com/zqu1992/ALQ