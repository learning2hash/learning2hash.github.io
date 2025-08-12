---
layout: publication
title: Learnable Fourier Features For Multi-dimensional Spatial Positional Encoding
authors: Yang Li, Si Si, Gang Li, Cho-Jui Hsieh, Samy Bengio
conference: Arxiv
year: 2021
bibkey: li2021learnable
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.02795'}]
tags: []
short_authors: Li et al.
---
Attentional mechanisms are order-invariant. Positional encoding is a crucial
component to allow attention-based deep model architectures such as Transformer
to address sequences or images where the position of information matters. In
this paper, we propose a novel positional encoding method based on learnable
Fourier features. Instead of hard-coding each position as a token or a vector,
we represent each position, which can be multi-dimensional, as a trainable
encoding based on learnable Fourier feature mapping, modulated with a
multi-layer perceptron. The representation is particularly advantageous for a
spatial multi-dimensional position, e.g., pixel positions on an image, where
\(L_2\) distances or more complex positional relationships need to be captured.
Our experiments based on several public benchmark tasks show that our learnable
Fourier feature representation for multi-dimensional positional encoding
outperforms existing methods by both improving the accuracy and allowing faster
convergence.