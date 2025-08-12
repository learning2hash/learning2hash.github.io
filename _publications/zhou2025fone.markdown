---
layout: publication
title: 'Fone: Precise Single-token Number Embeddings Via Fourier Features'
authors: Tianyi Zhou, Deqing Fu, Mahdi Soltanolkotabi, Robin Jia, Vatsal Sharan
conference: Arxiv
year: 2025
bibkey: zhou2025fone
citations: 0
additional_links: [{name: Code, url: 'https://fouriernumber.github.io/'}, {name: Paper,
    url: 'https://arxiv.org/abs/2502.09741'}]
tags: []
short_authors: Zhou et al.
---
Large Language Models (LLMs) typically represent numbers using multiple
tokens, which requires the model to aggregate these tokens to interpret
numerical values. This fragmentation makes both training and inference less
efficient and adversely affects the model's performance on number-related
tasks. Inspired by the observation that pre-trained LLMs internally learn
Fourier-like features for number tokens, we propose Fourier Number Embedding
(FoNE), a novel method that directly maps numbers into the embedding space with
their Fourier features. FoNE encodes each number as a single token with only
two embedding dimensions per digit, effectively capturing numerical values
without fragmentation. This compact representation accelerates both training
and inference. Compared to traditional subword and digit-wise embeddings, FoNE
not only reduces computational overhead but also achieves higher accuracy
across various numerical tasks including addition, subtraction and
multiplication. On 6-digit decimal addition, FoNE requires 64\(\times\) less data
to achieve 99% accuracy than subword and digit-wise embeddings while using
3\(\times\) and 6\(\times\) fewer tokens per number, respectively. Furthermore,
FoNE is the only method that yields 100% accuracy on over 100,000 test examples
for addition, subtraction, and multiplication. The codes and visualization are
available at https://fouriernumber.github.io/.