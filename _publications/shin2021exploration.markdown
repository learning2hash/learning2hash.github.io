---
layout: publication
title: Exploration Into Translation-equivariant Image Quantization
authors: Woncheol Shin, Gyubok Lee, Jiyoung Lee, Eunyi Lyou, Joonseok Lee, Edward
  Choi
conference: ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2023
bibkey: shin2021exploration
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.00384'}]
tags: ["ICASSP", "Quantization"]
short_authors: Shin et al.
---
This is an exploratory study that discovers the current image quantization
(vector quantization) do not satisfy translation equivariance in the quantized
space due to aliasing. Instead of focusing on anti-aliasing, we propose a
simple yet effective way to achieve translation-equivariant image quantization
by enforcing orthogonality among the codebook embeddings. To explore the
advantages of translation-equivariant image quantization, we conduct three
proof-of-concept experiments with a carefully controlled dataset: (1)
text-to-image generation, where the quantized image indices are the target to
predict, (2) image-to-text generation, where the quantized image indices are
given as a condition, (3) using a smaller training set to analyze sample
efficiency. From the strictly controlled experiments, we empirically verify
that the translation-equivariant image quantizer improves not only sample
efficiency but also the accuracy over VQGAN up to +11.9% in text-to-image
generation and +3.9% in image-to-text generation.