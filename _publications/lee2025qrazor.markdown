---
layout: publication
title: 'Qrazor: Reliable And Effortless 4-bit LLM Quantization By Significant Data
  Razoring'
authors: Dongyoung Lee, Seungkyu Choi, Ik Joon Chang
conference: Arxiv
year: 2025
bibkey: lee2025qrazor
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.13331'}]
tags: ["Quantization"]
short_authors: Dongyoung Lee, Seungkyu Choi, Ik Joon Chang
---
Large-scale language models (LLMs) excel in language processing tasks but
face deployment challenges due to high memory and computational demands. While
low-bit quantization, such as 4-bit techniques, offers a potential solution,
these methods often suffer from significant accuracy loss or require
considerable effort for implementation such as reordering, rotation, etc. To
address these challenges, we propose QRazor, a simple yet effective
quantization scheme that enables 4-bit quantization of weights, activations,
and KV cache in transformer-based LLMs. QRazor operates in two stages: first,
quantizing data using 8 or 16-bit integers as a basis with absolute max scaling
to preserve accuracy close to full-precision models, and second, compressing
the quantized data to 4-bit using our significant data razoring (SDR)
technique, which retains only the four most salient bits. Without any
additional requirment of fine-tuning or additional training, QRazor achieves
performance similar or better compared to state-of-the-art in 4-bit
quantization method, surpassing Smoothquant and QLLM by over 12 points and
Quarot(RTN) by more than 2.9 points in zero-shot reasoning task accuracy on the
LLaMA2-7B model. Additionally, we introduce an integer-based arithmetic unit
optimized for QRazor, allowing direct low-precision operations on SDR data
without decompression.