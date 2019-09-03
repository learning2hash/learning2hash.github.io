---
layout: publication
title: "Variable-Length Quantization Strategy for Hashing"
authors: Yang Shi, Xiushan Nie, Xin Zhou, Xiaoming Xi, Yilong Yin
conference: ICIP
year: 2019
bibkey: shi2019variable
additional_links:
   - {name: "PDF", url: "https://ieeexplore.ieee.org/document/8803270"}
tags: ["ICIP", "Quantisation", "Variable-Bit", "Multi-Bit"]
---
Hashing is widely used to solve fast Approximate Nearest Neighbor (ANN) search problems, involves converting the original real-valued samples to binary-valued representations. The conventional quantization strategies, such as Single-Bit Quantization and Multi-Bit quantization, are considered ineffective, because of their serious information loss. To address this issue, we propose a novel variable-length quantization (VLQ) strategy for hashing. In the proposed VLQ technique, we divide all samples into different regions in each dimension firstly given the real-valued features of samples. Then we compute the dispersion degrees of these regions. Subsequently, we attempt to optimally assign different number of bits to each dimensions to obtain the minimum dispersion degree. Our experiments show that the VLQ strategy achieves not only superior performance over the state-of-the-art methods, but also has a faster retrieval speed on public datasets.
