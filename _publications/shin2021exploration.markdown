---
layout: publication
title: Exploration Into Translation-equivariant Image Quantization
authors: Woncheol Shin et al.
conference: Arxiv
year: 2021
citations: 1
bibkey: shin2021exploration
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.00384'}]
tags: [Quantization, Tools and Libraries]
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